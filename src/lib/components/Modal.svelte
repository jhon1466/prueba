<script>
  import { createEventDispatcher } from 'svelte';

  const dispatch = createEventDispatcher();

  const closeModal = () => {
    dispatch('close');
  };
</script>

<div class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity dark:bg-gray-800">
  <div class="fixed inset-0 flex items-center justify-center p-4">
    <div class="bg-white dark:bg-gray-900 rounded-lg shadow-lg max-w-3xl mx-auto p-6 overflow-y-auto max-h-screen">
      <h2 class="text-2xl font-semibold mb-6 text-gray-900 dark:text-gray-100">Términos y Condiciones de Uso</h2>
      <div class="text-gray-700 dark:text-gray-300 overflow-y-auto max-h-96">
        <h3 class="text-xl font-semibold mt-4">1. Aceptación de los Términos</h3>
        <p>
          Al acceder y utilizar nuestra plataforma de Modelos de Lenguaje de Gran Escala (LLMs), usted acepta cumplir y estar sujeto a los siguientes términos y condiciones. Si no está de acuerdo con estos términos, no debe usar nuestra plataforma.
        </p>
        <h3 class="text-xl font-semibold mt-4">2. Descripción del Servicio</h3>
        <p>
          Nuestra plataforma proporciona acceso a LLMs que permiten la generación de texto y respuestas automatizadas similares a ChatGPT. Los usuarios pueden interactuar con estos modelos de manera gratuita o mediante una suscripción de pago. Los LLMs utilizados en nuestra plataforma son de código abierto y no fueron creados por nosotros.
        </p>
        <h3 class="text-xl font-semibold mt-4">3. Uso Aceptable</h3>
        <p>
          Usted se compromete a utilizar nuestra plataforma de manera responsable y ética. Ejemplos de uso indebido incluyen, pero no se limitan a:
        </p>
        <ul class="list-disc pl-6">
          <li><strong>Actividades Ilegales:</strong> Usar la plataforma para participar en actividades ilegales, como fraudes, estafas, distribución de malware, o cualquier otra actividad que viole las leyes locales, nacionales o internacionales.</li>
          <li><strong>Contenido Ofensivo:</strong> Generar o distribuir contenido que sea ofensivo, discriminatorio, difamatorio, o que incite al odio contra cualquier grupo o individuo basado en raza, etnia, religión, género, orientación sexual, discapacidad u otras características protegidas.</li>
          <li><strong>Spam y Phishing:</strong> Utilizar la plataforma para enviar mensajes no solicitados (spam) o para realizar actividades de phishing (intentar obtener información confidencial engañando a las personas).</li>
          <li><strong>Manipulación y Hackeo:</strong> Intentar manipular, hackear o comprometer la seguridad de la plataforma o de los modelos de lenguaje. Esto incluye cualquier intento de explotar vulnerabilidades de seguridad, acceder a datos no autorizados o interrumpir el funcionamiento normal del servicio.</li>
          <li><strong>Uso Comercial No Autorizado:</strong> Usar la plataforma para fines comerciales no autorizados, como la reventa del servicio sin permiso o la explotación de los modelos para obtener ganancias sin autorización explícita de [Nombre de tu Empresa/Plataforma].</li>
          <li><strong>Violación de Propiedad Intelectual:</strong> Generar, compartir o distribuir contenido que infrinja los derechos de propiedad intelectual de terceros, incluyendo derechos de autor, marcas registradas y patentes.</li>
        </ul>
        <h3 class="text-xl font-semibold mt-4">4. Acceso a Conversaciones</h3>
        <p>
          El creador de la plataforma puede acceder a las conversaciones de los usuarios bajo circunstancias específicas, tales como:
        </p>
        <ul class="list-disc pl-6">
          <li><strong>Seguridad:</strong> Para proteger la seguridad de la plataforma y de otros usuarios.</li>
          <li><strong>Investigación de Uso Indebido:</strong> Para investigar y actuar ante el uso indebido de la plataforma, incluyendo pero no limitado a actividades ilegales o violaciones de nuestros términos y condiciones.</li>
        </ul>
        <h3 class="text-xl font-semibold mt-4">5. Suspensión y Terminación de Cuentas</h3>
        <p>
          Nos reservamos el derecho de suspender, bloquear o eliminar su cuenta en cualquier momento y por cualquier motivo, incluyendo, sin limitación, la violación de estos términos. Esto incluye cuentas con suscripciones de pago. No se otorgarán reembolsos por el tiempo restante de la suscripción en caso de suspensión o terminación debido a uso indebido.
        </p>
        <h3 class="text-xl font-semibold mt-4">6. Propiedad Intelectual</h3>
        <p>
          Todos los derechos, títulos e intereses sobre la plataforma en sí y su funcionamiento pertenecen a [Nombre de tu Empresa/Plataforma]. Los modelos de lenguaje utilizados en nuestra plataforma son de código abierto y están sujetos a sus respectivas licencias. Usted no tiene derecho a copiar, modificar, distribuir o vender cualquier parte de la plataforma sin nuestra autorización expresa, excepto en lo que respecta a los modelos de lenguaje de código abierto, que se rigen por sus propias licencias.
        </p>
        <h3 class="text-xl font-semibold mt-4">7. Privacidad</h3>
        <p>
          Nos comprometemos a proteger su privacidad. Consulte nuestra Política de Privacidad para obtener más detalles sobre cómo recopilamos, usamos y protegemos su información personal.
        </p>
        <h3 class="text-xl font-semibold mt-4">8. Limitación de Responsabilidad</h3>
        <p>
          Nuestra plataforma se proporciona "tal cual" y "según disponibilidad". No garantizamos que la plataforma esté libre de errores, segura o ininterrumpida. No seremos responsables de cualquier daño directo, indirecto, incidental, especial, o consecuente que resulte del uso o la imposibilidad de usar la plataforma.
        </p>
        <h3 class="text-xl font-semibold mt-4">9. Cambios en los Términos</h3>
        <p>
          Nos reservamos el derecho de modificar estos términos en cualquier momento. Las modificaciones se publicarán en esta página y la fecha de revisión se actualizará. El uso continuado de la plataforma después de cualquier cambio constituye su aceptación de los nuevos términos.
        </p>
        <h3 class="text-xl font-semibold mt-4">10. Ley Aplicable</h3>
        <p>
          Estos términos se regirán e interpretarán de acuerdo con las leyes de [Tu País/Estado], sin dar efecto a ningún principio de conflictos de leyes.
        </p>
        <h3 class="text-xl font-semibold mt-4">11. Contacto</h3>
        <p>
          Si tiene alguna pregunta sobre estos términos, por favor contáctenos en [correo electrónico de contacto].
        </p>
        <h2 class="text-2xl font-semibold mt-8 mb-6 text-gray-900 dark:text-gray-100">Política de Privacidad</h2>
        <h3 class="text-xl font-semibold mt-4">1. Introducción</h3>
        <p>
          En [Nombre de tu Empresa/Plataforma], respetamos su privacidad y nos comprometemos a proteger su información personal. Esta política de privacidad explica cómo recopilamos, usamos y compartimos su información cuando usa nuestra plataforma de Modelos de Lenguaje de Gran Escala (LLMs).
        </p>
        <h3 class="text-xl font-semibold mt-4">2. Información que Recopilamos</h3>
        <p><strong>Información que Usted Proporciona</strong></p>
        <ul class="list-disc pl-6">
          <li><strong>Registro y Perfil:</strong> Cuando se registra en nuestra plataforma, recopilamos información como su nombre, dirección de correo electrónico y otros detalles de contacto.</li>
          <li><strong>Interacciones:</strong> Recopilamos las entradas de texto que proporciona cuando interactúa con los modelos, así como cualquier retroalimentación que ofrezca.</li>
        </ul>
        <p><strong>Información Recopilada Automáticamente</strong></p>
        <ul class="list-disc pl-6">
          <li><strong>Datos de Uso:</strong> Recopilamos información sobre su uso de la plataforma, incluyendo direcciones IP, tipo de dispositivo, navegador, páginas visitadas y tiempo de uso.</li>
          <li><strong>Cookies y Tecnologías Similares:</strong> Usamos cookies y tecnologías similares para recopilar información y mejorar su experiencia en nuestra plataforma.</li>
        </ul>
        <h3 class="text-xl font-semibold mt-4">3. Cómo Usamos su Información</h3>
        <p>
          Usamos la información que recopilamos para:
        </p>
        <ul class="list-disc pl-6">
          <li>Proveer y mejorar nuestra plataforma.</li>
          <li>Personalizar su experiencia.</li>
          <li>Comunicarnos con usted, responder a sus preguntas y proporcionar soporte.</li>
          <li>Monitorear y analizar el uso y las tendencias para mejorar la plataforma.</li>
          <li>Proteger la seguridad e integridad de la plataforma.</li>
        </ul>
        <h3 class="text-xl font-semibold mt-4">4. Acceso a Conversaciones</h3>
        <p>
          Tomamos muy en serio la privacidad de sus datos. Sin embargo, el creador de la plataforma puede acceder a las conversaciones de los usuarios bajo circunstancias específicas, tales como:
        </p>
        <ul class="list-disc pl-6">
          <li><strong>Seguridad:</strong> Para proteger la seguridad de la plataforma y de otros usuarios.</li>
          <li><strong>Investigación de Uso Indebido:</strong> Para investigar y actuar ante el uso indebido de la plataforma, incluyendo pero no limitado a actividades ilegales o violaciones de nuestros términos y condiciones.</li>
        </ul>
        <h3 class="text-xl font-semibold mt-4">5. Compartir su Información</h3>
        <p>
          No vendemos su información personal a terceros. Podemos compartir su información con terceros solo en las siguientes circunstancias:
        </p>
        <ul class="list-disc pl-6">
          <li><strong>Proveedores de Servicios:</strong> Compartimos información con proveedores de servicios que nos ayudan a operar y mejorar nuestra plataforma.</li>
          <li><strong>Requisitos Legales:</strong> Podemos divulgar su información si creemos que es necesario para cumplir con una ley, regulación o proceso legal aplicable.</li>
          <li><strong>Protección de Derechos:</strong> Podemos divulgar su información para proteger los derechos, propiedad o seguridad de [Nombre de tu Empresa/Plataforma], nuestros usuarios u otros.</li>
        </ul>
        <h3 class="text-xl font-semibold mt-4">6. Seguridad de su Información</h3>
        <p>
          Tomamos medidas razonables para proteger su información personal contra pérdida, robo, uso indebido y acceso no autorizado. Sin embargo, no podemos garantizar la seguridad completa de la información transmitida a través de Internet.
        </p>
        <h3 class="text-xl font-semibold mt-4">7. Sus Derechos</h3>
        <p>
          Dependiendo de su jurisdicción, puede tener ciertos derechos respecto a su información personal, incluyendo el derecho a acceder, corregir o eliminar su información. Para ejercer estos derechos, por favor contáctenos en [correo electrónico de contacto].
        </p>
        <h3 class="text-xl font-semibold mt-4">8. Retención de Datos</h3>
        <p>
          Retenemos su información personal durante el tiempo que sea necesario para cumplir con los propósitos descritos en esta política, a menos que la ley exija o permita un período de retención más largo.
        </p>
        <h3 class="text-xl font-semibold mt-4">9. Cambios en esta Política</h3>
        <p>
          Podemos actualizar esta política de privacidad de vez en cuando. Publicaremos cualquier cambio en esta página y actualizaremos la fecha de revisión. Su uso continuado de la plataforma después de cualquier cambio constituye su aceptación de la nueva política de privacidad.
        </p>
        <h3 class="text-xl font-semibold mt-4">10. Contacto</h3>
        <p>
          Si tiene preguntas o inquietudes sobre esta política de privacidad, por favor contáctenos en [correo electrónico de contacto].
        </p>
      </div>
      <button on:click={closeModal} class="mt-6 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-300">
        Cerrar
      </button>
    </div>
  </div>
</div>
