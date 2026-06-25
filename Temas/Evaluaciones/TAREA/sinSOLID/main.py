from TAREA.sinSOLID.Controller.controladorNotificaciones import ControladorNotificaciones

controladorSistema = ControladorNotificaciones()
controladorSistema.iniciar()

# 1. ¿Qué responsabilidades están mezcladas en la misma clase?
""" En la clase SistemaNotificaciones se mezclan varias responsabilidades,
    ya que muestra el menú, solicita datos al usuario, valida la información,
    procesa las notificaciones y guarda el historial."""

# 2. ¿Qué ocurriría si la empresa quiere agregar un nuevo canal de comunicación?
"""" Sería necesario modificar directamente el método procesarNotificacion,
     agregando una nueva condición if o elif. Esto hace que el sistema no sea
     flexible ni fácil de extender."""

# 3. ¿Qué partes del sistema están altamente acopladas?
""" El controlador está altamente acoplado al asdas, porque depende directamente
    de la clase SistemaNotificaciones. Además, el procesamiento está amarrado
    a opciones específicas mediante condicionales."""

# 4. ¿Dónde se violan los principios SOLID?
"""Se viola SRP porque una sola clase tiene muchas responsabilidades.
   Se viola OCP porque para agregar un nuevo canal hay que modificar código existente.
   Se viola DIP porque el controlador depende de una implementación concreta."""

# 5. ¿Qué partes del sistema deberían separarse?
"""Deberían separarse la interacción con el usuario, la lógica de control,
   la lógica de envío de notificaciones y el manejo de cada canal de comunicación."""