<script setup></script>

<template>
  <footer class="footer">
    <div class="footer__container g-container">
      <article class="footer__social">
        <img src="@/assets/svg/1c-logo.svg" />
        <ul class="socials">
          <li>
            <a href="#">
              <img src="@/assets/svg/facebook-icon.svg" />
            </a>
          </li>
          <li>
            <a href="#">
              <img src="@/assets/svg/twitter-icon.svg" />
            </a>
          </li>
          <li>
            <a href="#">
              <img src="@/assets/svg/instagram-icon.svg" />
            </a>
          </li>
          <li>
            <a href="#">
              <img src="@/assets/svg/linkedIn-icon.svg" />
            </a>
          </li>
          <li>
            <a href="#">
              <img src="@/assets/svg/tiktok-icon.svg" />
            </a>
          </li>
          <li>
            <a href="#">
              <img src="@/assets/svg/telegram-icon.svg" />
            </a>
          </li>
        </ul>
      </article>
      <article id="help" class="footer__get-help">
        <h3 class="ul-title">Помощь</h3>
        <ul>
          <li>
            <a href="https://t.me/Elvira1C">Elvira1C</a>
          </li>
          <li>
            <a href="https://t.me/Justiks1337">Justiks</a>
          </li>
          <li>
            <a href="https://psy-sovet.ru/">Помощь</a>
          </li>
          <li>
            <a href="https://t.me/kult_sviney">Группа</a>
          </li>
        </ul>
      </article>
      <article id="contacts" class="footer__contacts">
        <h3 class="ul-title">Контакты разработчиков</h3>
        <ul>
          <li>
            <a href="https://t.me/Justiks1337"> Дубков Максим</a>
          </li>
          <li>
            <a href="mailto:sasaprigoda6@gmail.com"> sasaprigoda6@gmail.com</a>
          </li>
          <li>
            <a href="https://kazoe.ru/contacts"> sodiel</a>
          </li>
        </ul>
      </article>
      <article id="project_resources" class="footer__info">
        <p class="footer__info-copyright">
          © 2023 1с учебный центр, Все Права Защищены
        </p>
        <ul>
          <li><a href="https://t.me/OneC_chess_bot">Бот</a></li>
          <li>
            <a href="https://github.com/Justiks228/ChessBot">Код проекта</a>
          </li>
        </ul>
      </article>
    </div>
  </footer>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_mixins.scss";
@import "@/assets/scss/_variables.scss";
.footer {
  background-color: $dark-gray;

  &__container {
    padding-top: 32px;
    padding-bottom: 0;

    display: flex;
    justify-content: space-between;
    align-items: start;
    flex-flow: row wrap;
    row-gap: 32px;
  }

  &__social {
    display: flex;
    flex-flow: column nowrap;
    row-gap: 24px;

    & > .socials {
      width: max-content;
      & > li {
        display: inline-block;
        margin-top: 0;
        &:not(:first-child) {
          margin-left: 12px;
        }
        & > a {
          &::before {
            display: none !important; // на всякий случай
          }
          & > img {
            vertical-align: middle;
          }
        }
      }
    }
  }

  .ul-title {
    color: #fff;
    font-family: "Poppins", sans-serif;
    @extend %text-20;
    text-transform: uppercase;
  }

  ul > li {
    margin-top: 16px;

    & > a {
      color: $light-gray;
      @extend %text-16;
    }
  }

  &__info {
    flex: 0 0 100%;

    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
    align-items: center;

    padding-bottom: 16px;

    &-copyright {
      color: $light-gray;
      @extend %text-16;
    }

    & > ul > li {
      display: inline-block;
      margin-top: 0;
      &:not(:first-child) {
        margin-left: 24px;
      }
    }
  }
}

@media (hover: hover) {
  ul > li > a {
    @include link($light-gray);
  }

  .footer__social {
    .socials img {
      vertical-align: middle;
      transform: scale(1);
      transition: all 0.5s ease-in-out;
    }
    .socials a:hover > img {
      transform: scale(1.1);
    }
  }
}
@media (width <= 1160px) {
  .footer {
    &__container {
      padding-top: 32px;
      padding-bottom: 0;
      row-gap: 24px;
    }

    &__social {
      width: 100%;
      align-items: start;
    }

    &__info {
      padding-top: 8px; // container row-gap and padding
      flex-direction: column;
      row-gap: 24px;
      align-items: center;
    }
  }
}
@media (width <= 674px) {
  .footer {
    &__container {
      display: block;
      padding-top: 32px;
      padding-bottom: 0;
      row-gap: 24px;

      & > * {
        display: block;
      }

      & > *:not(:first-child) {
        margin-top: 24px;
      }

      & > *:last-child {
        margin-top: 32px;
      }
    }

    &__social {
      display: block;

      & > *:not(:first-child) {
        margin-top: 24px;
      }
    }

    &__info {
      padding: 16px 0;

      &-copyright {
        width: 210px;
      }

      & > ul > li {
        display: block;
        margin-top: 24px;
        &:not(:first-child) {
          margin-left: 0;
        }
      }
    }
  }
}

@media (width <= 410px) {
  .footer .ul-title {
    font-size: 18px;
    line-height: 26px;
  }
  .footer__info ul > li {
    margin-top: 12px;
    &:first-child {
      margin-top: 20px;
    }
  }
}
</style>
