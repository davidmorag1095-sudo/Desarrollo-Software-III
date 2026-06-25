import tkinter as tk
from tkinter import ttk, messagebox


class Normalizador:

    def __init__(self, root):
        self.root = root
        self.root.title("Normalizador Científico de Bases de Datos (1FN - 2FN - 3FN)")
        self.root.geometry("1250x900")

        # Configuración estética
        style = ttk.Style()
        style.configure("TLabelframe.Label", font=("Helvetica", 10, "bold"))

        # ================= FORMULARIO UNIVERSAL VACÍO =================
        form = ttk.LabelFrame(root, text=" Ingreso de Tabla Universal y Reglas ")
        form.pack(fill="x", padx=15, pady=10)
        form.columnconfigure(1, weight=1)

        # 1. Nombre de la tabla
        ttk.Label(form, text="Nombre de Tabla:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.nombre = ttk.Entry(form, font=("Segoe UI", 10))
        self.nombre.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # 2. Atributos globales
        ttk.Label(form, text="Atributos (separados por comas):").grid(row=1, column=0, sticky="nw", padx=5, pady=5)
        self.atributos = tk.Text(form, height=2, width=80, font=("Segoe UI", 10))
        self.atributos.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # 3. Relaciones entre Atributos
        ttk.Label(form, text="Relaciones / Cardinalidad:\n(Ej: id_estudiante - id_curso -> N:M)").grid(row=2, column=0,
                                                                                                       sticky="nw",
                                                                                                       padx=5, pady=5)
        self.relaciones = tk.Text(form, height=3, width=80, font=("Consolas", 10))
        self.relaciones.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # 4. Clave Primaria
        ttk.Label(form, text="Clave Primaria (separada por comas):").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.pk = ttk.Entry(form, font=("Segoe UI", 10))
        self.pk.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        # 5. Dependencias Funcionales
        ttk.Label(form, text="Dependencias Funcionales (A -> B):\n* Una por línea *").grid(row=4, column=0, sticky="nw",
                                                                                           padx=5, pady=5)
        self.df = tk.Text(form, height=5, width=80, font=("Consolas", 10))
        self.df.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        # ================= BOTONES DE ACCIÓN =================
        btns = ttk.Frame(form)
        btns.grid(row=5, column=1, pady=10, sticky="e")

        ttk.Button(btns, text="Normalizar Tabla", command=self.normalizar).pack(side="left", padx=5)
        ttk.Button(btns, text="Limpiar Todo", command=self.limpiar).pack(side="left", padx=5)

        # ================= PESTAÑAS DE RESULTADOS =================
        self.tabs = ttk.Notebook(root)
        self.tabs.pack(fill="both", expand=True, padx=15, pady=5)

        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tab3 = ttk.Frame(self.tabs)

        self.tabs.add(self.tab1, text=" 1FN (Primera Forma Normal) ")
        self.tabs.add(self.tab2, text=" 2FN (Segunda Forma Normal) ")
        self.tabs.add(self.tab3, text=" 3FN (Tercera Forma Normal) ")

    # ================= UI INTERNA =================

    def limpiar_frame(self, frame):
        for w in frame.winfo_children():
            w.destroy()

    def crear_tabla_ui(self, parent, nombre, pk_attrs, otros_attrs, row, col, info_extra=""):
        frame = ttk.LabelFrame(parent, text=f" Tabla: {nombre} ")
        frame.grid(row=row, column=col, padx=15, pady=15, sticky="nw")

        pk_str = ", ".join(sorted(list(pk_attrs)))
        otros_str = ", ".join(sorted(list(otros_attrs)))

        texto_completo = f"CLAVE PRIMARIA:\n  ⚡ {pk_str}\n\nOTROS ATRIBUTOS:\n"
        if otros_str:
            texto_completo += "\n".join([f"  • {a}" for a in sorted(list(otros_attrs))])
        else:
            texto_completo += "  (Ninguno)"

        if info_extra:
            texto_completo += f"\n\n📢 {info_extra}"

        tk.Label(
            frame,
            text=texto_completo,
            font=("Consolas", 11),
            justify="left",
            anchor="w",
            bg="#fdfdfd",
            relief="solid",
            bd=1,
            padx=15,
            pady=15
        ).pack(padx=10, pady=10)

    # ================= PARSEADORES DE TEXTO =================

    def parse_df(self, text):
        raw_dfs = {}
        for linea in text.strip().split("\n"):
            if not linea.strip() or "->" not in linea:
                continue
            izquierda, derecha = linea.split("->")
            lhs = frozenset(x.strip() for x in izquierda.split(",") if x.strip())
            rhs = set(x.strip() for x in derecha.split(",") if x.strip())

            if lhs not in raw_dfs:
                raw_dfs[lhs] = set()
            raw_dfs[lhs].update(rhs)
        return [(set(lhs), rhs) for lhs, rhs in raw_dfs.items()]

    def procesar_relaciones_pk(self, text, pk_actual):
        claves_detectadas = set(pk_actual)
        for linea in text.strip().split("\n"):
            if "N:M" in linea or "M:N" in linea:
                parte_atributos = linea.split("->")[0] if "->" in linea else linea
                parte_atributos = parte_atributos.replace("-", ",").split(",")
                for attr in parte_atributos:
                    clean_attr = attr.strip()
                    if clean_attr and "N:M" not in clean_attr and "M:N" not in clean_attr:
                        claves_detectadas.add(clean_attr)
        return claves_detectadas

    # ================= LÓGICA DE NORMALIZACIÓN MEJORADA =================

    def normalizar(self):
        nombre_base = self.nombre.get().strip().upper()
        attrs = set(a.strip() for a in self.atributos.get("1.0", tk.END).split(",") if a.strip())
        pk_inicial = set(x.strip() for x in self.pk.get().split(",") if x.strip())

        pk = self.procesar_relaciones_pk(self.relaciones.get("1.0", tk.END), pk_inicial)
        dfs = self.parse_df(self.df.get("1.0", tk.END))

        if not nombre_base or not attrs or not pk:
            messagebox.showerror("Error", "Por favor completa el Nombre, Atributos y Clave Primaria.")
            return

        if not pk.issubset(attrs):
            messagebox.showerror("Error", "La Clave Primaria contiene atributos que no están en la lista global.")
            return

        if pk != pk_inicial:
            self.pk.delete(0, tk.END)
            self.pk.insert(0, ", ".join(sorted(list(pk))))

        self.limpiar_frame(self.tab1)
        self.limpiar_frame(self.tab2)
        self.limpiar_frame(self.tab3)

        # ----------------- 1FN -----------------
        # Muestra la tabla original con todos los campos agrupados bajo la PK principal.
        self.crear_tabla_ui(self.tab1, f"{nombre_base}_1FN", pk, attrs - pk, 0, 0, "Todos los atributos son atómicos.")

        # ----------------- 2FN -----------------
        tablas_2fn_fusionadas = {}
        atributos_removidos_2fn = set()

        # Ocurre dependencia parcial SOLO si la PK tiene más de un elemento
        if len(pk) > 1:
            for lhs, rhs in dfs:
                # Si el lado izquierdo es parte de la PK, pero no es la PK completa
                if lhs.issubset(pk) and lhs != pk and len(lhs) > 0:
                    dependientes_validos = (rhs & attrs) - pk
                    if dependientes_validos:
                        key_lhs = frozenset(lhs)
                        if key_lhs not in tablas_2fn_fusionadas:
                            tablas_2fn_fusionadas[key_lhs] = set()
                        tablas_2fn_fusionadas[key_lhs].update(dependientes_validos)
                        atributos_removidos_2fn.update(dependientes_validos)

        lista_final_2fn = []
        tabla_principal_2fn_attrs = (attrs - pk) - atributos_removidos_2fn

        # Añadir la tabla principal modificada
        lista_final_2fn.append({
            "nombre": f"{nombre_base}_PRINCIPAL_2FN",
            "pk": pk,
            "attrs": tabla_principal_2fn_attrs,
            "info": "Mantiene atributos con dependencia completa."
        })

        # Añadir las subtablas que nacieron de las dependencias parciales
        idx = 1
        for k_pk, k_attrs in tablas_2fn_fusionadas.items():
            lista_final_2fn.append({
                "nombre": f"SUBTABLA_2FN_{idx}",
                "pk": set(k_pk),
                "attrs": k_attrs,
                "info": f"Creada por dependencia parcial de: {list(k_pk)}"
            })
            idx += 1

        # Si no hubo dependencias parciales (o PK era simple), hereda directo de la 1FN
        if len(lista_final_2fn) == 1 and len(pk) == 1:
            lista_final_2fn[0]["info"] = "Ya está en 2FN automáticamente (Clave Primaria Simple)."

        for col, t in enumerate(lista_final_2fn):
            self.crear_tabla_ui(self.tab2, t["nombre"], t["pk"], t["attrs"], 0, col, t["info"])

        # ----------------- 3FN -----------------
        lista_final_3fn = []
        contador_transitivas = 1

        # Procesamos cada una de las tablas obtenidas en la 2FN
        for esquema_2fn in lista_final_2fn:
            epk = esquema_2fn["pk"]
            eattrs = esquema_2fn["attrs"].copy()

            transitivas_locales = {}
            atributos_removidos_3fn = set()

            for lhs, rhs in dfs:
                # Una dependencia transitiva ocurre si X -> Y, donde X NO contiene a la clave primaria
                if lhs.issubset(epk | eattrs) and not epk.issubset(lhs):
                    dependientes_validos = (rhs & eattrs) - epk - lhs
                    if dependientes_validos:
                        key_lhs = frozenset(lhs)
                        if key_lhs not in transitivas_locales:
                            transitivas_locales[key_lhs] = set()
                        transitivas_locales[key_lhs].update(dependientes_validos)
                        atributos_removidos_3fn.update(dependientes_validos)

            # Guardamos la versión limpia de esta tabla
            info_base = "Limpia de dependencias transitivas." if atributos_removidos_3fn else "No requería cambios en 3FN."
            lista_final_3fn.append({
                "nombre": f"T_{esquema_2fn['nombre']}_BASE",
                "pk": epk,
                "attrs": eattrs - atributos_removidos_3fn,
                "info": info_base
            })

            # Guardamos las nuevas tablas transitivas
            for tk_lhs, tk_rhs in transitivas_locales.items():
                lista_final_3fn.append({
                    "nombre": f"RELACION_TRANSITIVA_{contador_transitivas}",
                    "pk": set(tk_lhs),
                    "attrs": tk_rhs,
                    "info": f"Extraída por dependencia transitiva de: {list(tk_lhs)}"
                })
                contador_transitivas += 1

        for col, t in enumerate(lista_final_3fn):
            self.crear_tabla_ui(self.tab3, t["nombre"], t["pk"], t["attrs"], 0, col, t["info"])

    # ================= LIMPIAR =================

    def limpiar(self):
        self.nombre.delete(0, tk.END)
        self.atributos.delete("1.0", tk.END)
        self.relaciones.delete("1.0", tk.END)
        self.pk.delete(0, tk.END)
        self.df.delete("1.0", tk.END)

        self.limpiar_frame(self.tab1)
        self.limpiar_frame(self.tab2)
        self.limpiar_frame(self.tab3)


if __name__ == "__main__":
    root = tk.Tk()
    app = Normalizador(root)
    root.mainloop()