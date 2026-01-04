/* * script.js
 * Responsável pelo roteamento (SPA), interações de menu e formulários.
 */

// 1. ROUTER: Função que alterna entre as Views (Home / Residential)
function router(pageName) {
    // Passo 1: Seleciona as Views
    const homeView = document.getElementById('view-home');
    const resView = document.getElementById('view-residential');

    // Passo 2: Esconde tudo primeiro (Reset)
    homeView.classList.add('page-hidden');
    homeView.classList.remove('page-visible');
    
    resView.classList.add('page-hidden');
    resView.classList.remove('page-visible');

    // Passo 3: Mostra apenas a escolhida
    const selected = document.getElementById('view-' + pageName);
    
    if (selected) {
        selected.classList.remove('page-hidden');
        selected.classList.add('page-visible');
        
        // UX: Rola para o topo para dar sensação de nova página
        window.scrollTo(0, 0);
    }
}

// 2. FORM HANDLER: Intercepta o envio e dá feedback visual
const form = document.getElementById('quote-form');

if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Impede o refresh da página
        
        const btn = this.querySelector('button[type="submit"]');
        const originalContent = btn.innerHTML;

        // Estado de Carregamento (Loading)
        // Note: SVG de loading simplificado para JS puro
        btn.innerHTML = 'Wait... Sending...';
        btn.disabled = true;
        btn.classList.add('opacity-75', 'cursor-not-allowed');

        // Simula delay de rede (1.5 segundos)
        setTimeout(() => {
            // Estado de Sucesso
            btn.innerHTML = 'Message Sent! ✅';
            btn.classList.remove('bg-brand-600', 'hover:bg-brand-700');
            btn.classList.add('bg-green-600', 'hover:bg-green-700');

            // Limpa o form e reseta o botão após 2 segundos
            setTimeout(() => {
                this.reset();
                btn.innerHTML = originalContent;
                btn.disabled = false;
                btn.classList.remove('opacity-75', 'cursor-not-allowed', 'bg-green-600', 'hover:bg-green-700');
                btn.classList.add('bg-brand-600', 'hover:bg-brand-700');
                alert("Thanks! We will contact you shortly.");
            }, 2000);
        }, 1500);
    });
}

// 3. MOBILE MENU: Lógica do botão hambúrguer
const mobileBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener('click', () => {
        // Toggle: Se tem a classe 'hidden', tira. Se não tem, coloca.
        mobileMenu.classList.toggle('hidden');
    });
}