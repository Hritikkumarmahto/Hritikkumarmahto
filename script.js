/*-----------Mixiitup-------*/
let mixerProjects = mixitup('.project__container', {
    selectors: {
        target: '.project__item'
    },
    animation: {
        duration: 300
    }
});

/* -------------Active work-------*/

const linkWork = document.querySelectorAll('.category__btn');

function activeWork() {
    linkWork.forEach((a) => a.classList.remove('active-work'))
    this.classList.add('active-work');
}
linkWork.forEach((a) => a.addEventListener('click', activeWork));

/*---------Testimonials swiper ------------*/
var testiSwiper = new Swiper('.testimonial__container', {
    loop: true,
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
    pagination: {
        el: ".swiper-pagination",
    },
    mousewheel: true,
    keyboard: true,
});

/*--------------------------email js-------------------*/
const contactForm = document.getElementById('contact-form'),
    contactName = document.getElementById('contact-name'),
    contactEmail = document.getElementById('contact-email'),
    Message = document.getElementById('message'),
    contactMessage = document.getElementById('contact-message');
const sendEmail = (e) => {
    e.preventDefault();

    //check if the filed has a value

    if (contactName.value === '' || contactEmail.value === '' || Message.value === '') {
        //add and remove color
        contactMessage.classList.remove('color-light');
        contactMessage.classList.add('color-dark');

        //show message

        contactMessage.textContent='Write all the input fields';

    }
    else{
        //serviceId-templateId-#from -publickey
        emailjs.sendForm('','','','')
    }
}
contactForm.addEventListener('submit',sendEmail);