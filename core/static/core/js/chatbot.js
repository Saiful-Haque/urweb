// ================================================
//  URWEB AI Chatbot - Rule-Based Response Engine
// ================================================

const URWEB_RESPONSES = [
    {
        patterns: ['hello', 'hi', 'hey', 'good morning', 'good evening', 'howdy', 'sup'],
        reply: "Hi there! 👋 I'm the URWEB AI assistant. I can help you with information about our services, pricing, portfolio, and more. What would you like to know?",
        quick: ['Our Services', 'Get a Quote', 'View Portfolio']
    },
    {
        patterns: ['service', 'services', 'what do you do', 'offer', 'offer', 'help with', 'work'],
        reply: "URWEB offers a full suite of digital services:\n\n• 🖥️ **Web Design & Development**\n• 📱 **Mobile App Development**\n• 🛍️ **E-commerce Solutions**\n• ⚡ **Digital Marketing & SEO**\n• ☁️ **Cloud & DevOps Solutions**\n• 🔒 **Cybersecurity Consulting**\n\nWould you like to learn more about any of these?",
        quick: ['Pricing', 'Get a Quote', 'View Portfolio']
    },
    {
        patterns: ['price', 'pricing', 'cost', 'how much', 'rate', 'package', 'plan', 'fee'],
        reply: "We have flexible pricing plans designed for every stage of growth:\n\n💚 **Starter** — $99/mo (Perfect for individuals)\n🔵 **Professional** — $199/mo (Best for growing businesses)\n🔴 **Enterprise** — Custom (Full-scale solutions)\n\nAll plans include dedicated support and monthly reports!",
        quick: ['View All Plans', 'Get a Quote', 'Our Services']
    },
    {
        patterns: ['portfolio', 'project', 'work', 'example', 'past', 'previous', 'showcase'],
        reply: "We've built amazing digital experiences across multiple industries — from fintech platforms to e-commerce stores and SaaS dashboards. 🚀\n\nCheck out our full portfolio to see case studies, technologies used, and results delivered.",
        quick: ['View Portfolio', 'Get a Quote']
    },
    {
        patterns: ['about', 'team', 'who are you', 'company', 'urweb', 'story', 'founded'],
        reply: "URWEB is a full-service digital agency specializing in building high-performance, scalable websites and apps for ambitious brands. 💡\n\nOur expert team brings together design, engineering, and strategy to deliver results that matter.",
        quick: ['Our Services', 'Meet the Team', 'Contact Us']
    },
    {
        patterns: ['contact', 'reach', 'email', 'phone', 'talk', 'speak', 'get in touch', 'call'],
        reply: "Ready to start your project? We'd love to hear from you! 📬\n\nYou can reach us via our contact form, and our team will get back to you within 24 hours.",
        quick: ['Contact Us', 'Get a Quote']
    },
    {
        patterns: ['quote', 'estimate', 'proposal', 'scope', 'consult', 'free', 'enquiry'],
        reply: "Awesome! Getting a quote is easy and completely free. 🎯\n\nJust share a brief overview of your project on our contact page and our team will prepare a custom proposal for you within 1 business day.",
        quick: ['Get a Quote', 'View Portfolio']
    },
    {
        patterns: ['seo', 'marketing', 'rank', 'google', 'search', 'traffic', 'visibility'],
        reply: "Our digital marketing team specializes in SEO, content strategy, and paid campaigns that drive real traffic and qualified leads to your business. 📈\n\nWe've helped clients achieve 10x organic growth in under 6 months!",
        quick: ['Our Services', 'Get a Quote']
    },
    {
        patterns: ['ecommerce', 'shopify', 'store', 'shop', 'sell', 'woocommerce', 'product'],
        reply: "We build lightning-fast, conversion-optimized e-commerce stores using Shopify, WooCommerce, and custom platforms. 🛍️\n\nFrom product catalog to checkout and fulfilment integrations — we handle it all.",
        quick: ['Get a Quote', 'View Portfolio']
    },
    {
        patterns: ['app', 'mobile', 'ios', 'android', 'react native', 'flutter'],
        reply: "We develop high-quality cross-platform mobile apps for iOS and Android using React Native and Flutter. 📱\n\nFrom MVPs to full-scale apps with backend APIs — we've got your stack covered.",
        quick: ['Our Services', 'Get a Quote']
    },
    {
        patterns: ['support', 'maintenance', 'bug', 'fix', 'update', 'maintain', 'issue'],
        reply: "We provide ongoing support and maintenance plans to keep your digital products running at peak performance. 🔧\n\nAll Professional and Enterprise plan clients get priority support with < 4 hour response times.",
        quick: ['View Plans', 'Contact Us']
    },
    {
        patterns: ['dashboard', 'admin', 'login', 'portal', 'crm'],
        reply: "Our client portal gives you real-time visibility into your project's progress, milestones, and communication threads. 🖥️\n\nLog in to access your dashboard, or contact us to get set up.",
        quick: ['Contact Us', 'Get a Quote']
    },
    {
        patterns: ['timeline', 'long', 'delivery', 'deadline', 'turnaround', 'quick', 'fast'],
        reply: "Project timelines vary based on scope:\n\n⚡ Landing Pages: 3–5 days\n🌐 Full Websites: 2–4 weeks\n🛍️ E-commerce: 3–6 weeks\n📱 Mobile Apps: 6–14 weeks\n\nWe always deliver on time — or earlier. Rush timelines available!",
        quick: ['Get a Quote', 'Contact Us']
    },
    {
        patterns: ['thank', 'thanks', 'awesome', 'great', 'perfect', 'helpful', 'nice'],
        reply: "You're very welcome! 😊 We're here anytime you need us. Is there anything else I can help you with?",
        quick: ['Our Services', 'Get a Quote', 'Contact Us']
    },
    {
        patterns: ['bye', 'goodbye', 'see you', 'later', 'exit', 'close'],
        reply: "Thanks for chatting with us! 👋 Have a wonderful day. Feel free to reach out anytime — we're always here to help!",
        quick: []
    }
];

const QUICK_LINKS = {
    'Our Services':    '/services/',
    'Get a Quote':     '/contact/',
    'View Portfolio':  '/portfolio/',
    'Pricing':         '/pricing/',
    'View All Plans':  '/pricing/',
    'View Plans':      '/pricing/',
    'Contact Us':      '/contact/',
    'Meet the Team':   '/about/',
};

const FALLBACK = {
    reply: "That's a great question! I'm still learning, but I'm sure one of our team members can help. 💬\n\nWould you like to get in touch with us directly? We typically respond within a few hours.",
    quick: ['Contact Us', 'Our Services', 'Get a Quote']
};

// ================================================
//  Chatbot Engine
// ================================================

(function () {

    function getResponse(text) {
        const lower = text.toLowerCase().trim();
        for (const item of URWEB_RESPONSES) {
            if (item.patterns.some(p => lower.includes(p))) {
                return item;
            }
        }
        return FALLBACK;
    }

    function formatText(text) {
        return text
            .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
            .replace(/\n/g, '<br>');
    }

    function appendMessage(role, text, messagesEl) {
        const wrapper = document.createElement('div');
        wrapper.className = `chat-msg ${role}`;

        if (role === 'bot') {
            const avatar = document.createElement('div');
            avatar.className = 'msg-avatar';
            avatar.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a4 4 0 0 1 4 4 4 4 0 0 1-4 4 4 4 0 0 1-4-4 4 4 0 0 1 4-4M8 14h8a4 4 0 0 1 4 4v2H4v-2a4 4 0 0 1 4-4Z" fill="white"/></svg>`;
            wrapper.appendChild(avatar);
        }

        const bubble = document.createElement('div');
        bubble.className = 'msg-bubble';
        bubble.innerHTML = formatText(text);
        wrapper.appendChild(bubble);

        messagesEl.appendChild(wrapper);
        messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function showTyping(messagesEl) {
        const wrapper = document.createElement('div');
        wrapper.className = 'chat-msg bot';
        wrapper.id = 'typing-indicator';

        const avatar = document.createElement('div');
        avatar.className = 'msg-avatar';
        avatar.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a4 4 0 0 1 4 4 4 4 0 0 1-4 4 4 4 0 0 1-4-4 4 4 0 0 1 4-4M8 14h8a4 4 0 0 1 4 4v2H4v-2a4 4 0 0 1 4-4Z" fill="white"/></svg>`;
        wrapper.appendChild(avatar);

        const bubble = document.createElement('div');
        bubble.className = 'msg-bubble';
        bubble.innerHTML = `<div class="typing-indicator"><span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span></div>`;
        wrapper.appendChild(bubble);

        messagesEl.appendChild(wrapper);
        messagesEl.scrollTop = messagesEl.scrollHeight;
        return wrapper;
    }

    function renderQuickActions(quickList, actionsEl) {
        actionsEl.innerHTML = '';
        quickList.forEach(label => {
            const btn = document.createElement('button');
            btn.className = 'quick-btn';
            btn.textContent = label;
            btn.addEventListener('click', () => {
                const url = QUICK_LINKS[label];
                if (url) {
                    window.location.href = url;
                }
            });
            actionsEl.appendChild(btn);
        });
    }

    function sendMessage(input, messagesEl, actionsEl) {
        const text = input.value.trim();
        if (!text) return;

        appendMessage('user', text, messagesEl);
        input.value = '';

        const typing = showTyping(messagesEl);

        setTimeout(() => {
            typing.remove();
            const response = getResponse(text);
            appendMessage('bot', response.reply, messagesEl);
            renderQuickActions(response.quick || [], actionsEl);
        }, 900 + Math.random() * 400);
    }

    window.addEventListener('DOMContentLoaded', function () {
        const fab     = document.getElementById('chatbot-fab');
        const window_ = document.getElementById('chatbot-window');
        const closeBtn= document.getElementById('chat-close-btn');
        const messages= document.getElementById('chat-messages');
        const input   = document.getElementById('chat-input');
        const sendBtn = document.getElementById('chat-send-btn');
        const actions = document.getElementById('chat-quick-actions');

        if (!fab) return;

        // Toggle open/close
        fab.addEventListener('click', () => {
            const isOpen = window_.classList.toggle('is-open');
            fab.classList.toggle('is-open', isOpen);
            // Hide notification badge on first open
            const badge = fab.querySelector('.fab-badge');
            if (badge && isOpen) badge.style.display = 'none';
            if (isOpen) input.focus();
        });

        closeBtn.addEventListener('click', () => {
            window_.classList.remove('is-open');
            fab.classList.remove('is-open');
        });

        // Send on button click
        sendBtn.addEventListener('click', () => sendMessage(input, messages, actions));

        // Send on Enter
        input.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage(input, messages, actions);
            }
        });
    });

})();
