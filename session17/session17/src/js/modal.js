// 📁 modal.js
// 모달 관련 함수들을 정의하고 내보낸다.
const $ = (selector) => document.querySelector(selector);
const modal = $(".modal-container");
const body = $("body");

const openModal =() => {
    modal.classList.add("open");
    body.style.overflow ="hidden";

};

const closeModal=() =>{
    modal.classList.remove("open");
    body.style.overflow ="auto";

};

export {openModal, closeModal};