// 📁 main.js
import { openModal, closeModal } from "./modal.js";
import { setCookie, getCookie } from "./cookie.js";

// JS에서 DOM element 가져올 때 관용적으로 $표시를 사용한다.
// $표시로 DOM element return해서 반복 줄이는 함수
const $ = (selector) => document.querySelector(selector);

function App() {
  // App 이라는 객체를 생성하고 그 App의 init이라는 메소드를 불러와서 로직을 실행될 수 있게끔 초기화 메소드를 만든다.
  this.init = () => {
    // 모달을 닫는 쿠키가 있는지 확인한다.
    if (getCookie("modal-closed") === "true") {
      return;
    }
    // 모달을 닫는 쿠기가 없다면 무조건 모달 닫기
    closeModal();
  };

  $(".btn-open-modal").addEventListener("click", () => {
    openModal();
  });

  $(".modal-container").addEventListener("click", (event) => {
    if (event.target === $(".modal-container")) {
      closeModal();
    }
  });

  $(".modal-close").addEventListener("click", () => {
    closeModal();
  });

}

// 페이지 최초로 접근했을 때 app 이라는 객체를 생성한다.
// new 연산자로 생성된 인스턴스는 하나의 라이프사이클을 가지고, 이거에 대한 개별적인 상태 관리가 가능해진다.
const app = new App();
// 그 app의 init이라는 메소드를 불러와서 로직을 실행될 수 있게끔 한다.
app.init();
