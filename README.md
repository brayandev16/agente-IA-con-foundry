# History Agent 📜🤖

Cliente de consola en Python para interactuar de forma segura con un agente de Inteligencia Artificial ("history-agent") desplegado en Azure AI Projects. Este proyecto sirve como interfaz local para comunicarte directamente con el modelo hospedado en la nube.

## 🎓 Certificación y Ruta de Aprendizaje

Este proyecto fue desarrollado como caso de estudio práctico para la ruta de aprendizaje de **Microsoft AI Skills**. 

🏆 **Certificación obtenida:** [Ver credencial oficial en Credly](https://www.credly.com/badges/d77a623a-a3ee-4258-860e-39d86ffb2c38)
## 🛠️ Con qué se construyó

- **Lenguaje:** Python 3
- **SDKs y Librerías:** 
  - `azure-ai-projects` (Gestión e interacción con el agente)
  - `azure-identity` (Autenticación nativa segura)
- **Infraestructura Cloud:** Azure AI Projects

## ⚙️ Cómo funciona

El script principal (`agent.py`) actúa como un puente entre tu terminal local y la infraestructura de Azure AI:

1. **Autenticación:** Utiliza `DefaultAzureCredential` para resolver el acceso de manera automática (por ejemplo, detectando tu sesión de Azure CLI), evitando exponer claves secretas (API Keys) en el código fuente.
2. **Conexión:** Se enlaza al endpoint del recurso `agentbrayanrodriguez-resource`.
3. **Ciclo Interactivo:** Inicia un bucle (REPL) en la consola que captura tu texto (`user_input`).
4. **Respuesta:** Empaqueta tu mensaje y se lo envía al modelo `history-agent` (versión 1). Luego, imprime la respuesta procesada por la Inteligencia Artificial.

## 💡 Para qué se puede usar

- **Pruebas rápidas (PoC):** Validar el comportamiento y las instrucciones (prompts) de tu agente en Azure antes de conectarlo a un frontend complejo web o móvil.
- **Herramienta de terminal:** Hacer consultas al agente directamente desde tu consola de comandos sin salir del entorno de desarrollo.
- **Plantilla base:** Usarlo como punto de partida para entender cómo integrar la SDK de Python con los servicios de OpenAI dentro del ecosistema de Microsoft Azure.

## 🚀 Cómo ejecutarlo localmente

1. Asegúrate de tener Python instalado y tu entorno virtual activo.
2. Instala las dependencias necesarias:
   ```bash
   pip install azure-ai-projects>=2.1.0 azure-identity
   ```
3. Autentícate en tu entorno local usando Azure CLI:
   ```bash
   az login
   ```
4. Ejecuta el agente:
   ```bash
   python agent.py
   ```
5. ¡Empieza a chatear! Cuando quieras terminar la sesión, escribe `quit`.
