<script setup></script>

<template>
  <footer class="footer">
    <div class="footer__container g-container">
      <article class="footer__social">
        <img src="/src/assets/svg/1c-logo.svg" alt="1С УЧЕБНЫЙ ЦЕНТР" />
        <ul class="socials">
          <li>
            <a href="#">
              <img src="/src/assets/svg/facebook-icon.svg" />
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
        <div class="footer__social-buttons">
          <a href="#" class="footer__social-store footer__social-store_google">
            <img
              src="@/assets/svg/google-store.svg"
              alt="Download in google store" />
          </a>
          <a href="#" class="footer__social-store footer__social-store_app">
            <img src="@/assets/svg/app-store.svg" alt="Download in app store" />
          </a>
        </div>
      </article>
      <article class="footer__get-help">
        <h3 class="ul-title">Get help</h3>
        <ul>
          <li>
            <a href="#">Order Status</a>
          </li>
          <li>
            <a href="#">Shipping and Delivery</a>
          </li>
          <li>
            <a href="#">Returns</a>
          </li>
          <li>
            <a href="#">Payment Options</a>
          </li>
          <li>
            <a href="#">Contact Us</a>
          </li>
        </ul>
      </article>
      <article class="footer__about">
        <h3 class="ul-title">About</h3>
        <ul>
          <li><a href="#">News</a></li>
          <li><a href="#">Careers</a></li>
          <li><a href="#">Investors</a></li>
          <li><a href="#">Sustainability</a></li>
        </ul>
      </article>
      <article class="footer__contacts">
        <h3 class="ul-title">Contacts</h3>
        <ul>
          <li>
            <a href="mailto:sasaprigoda6@gmail.com">sasaprigoda6@gmail.com</a>
          </li>
          <li><address href="#">Gadyach city, Hetmanska street 58</address></li>
          <li><a href="tel:+380663880963">+380663880963</a></li>
        </ul>
      </article>
      <article class="footer__info">
        <p class="footer__info-copyright">
          © 2023 1с учебный центр, All Rights Reserved
        </p>
        <ul>
          <li><a href="#">Terms of Use</a></li>
          <li><a href="#">Terms of Sale</a></li>
          <li><a href="#">Privacy & Cookie Policy</a></li>
          <li><a href="#">Cookie Settings</a></li>
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

    &-buttons {
      & > a {
        display: block;
      }
      & > a:not(:first-child) {
        margin-top: 24px;
      }
    }
  }

  .ul-title {
    color: #fff;
    font-family: "Poppins", sans-serif;
    @extend %text-20;
    text-transform: uppercase;
  }

  address {
    color: $light-gray;
    @extend %text-16;
    font-style: normal;
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
    &-store {
      & > img {
        transform: scale(1);
        transition: all 0.5s ease-in-out;
      }
      &:hover > img {
        transform: scale(1.1);
      }
    }

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
      display: grid;
      width: 100%;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      justify-content: space-between;
      &-buttons {
        grid-column: 2/2;
        grid-row: 1/3;
        align-self: center;
        justify-self: end;
        & > a {
          display: inline-block;
          &:not(:first-child) {
            margin-top: 0;
            margin-left: 24px;
          }
        }
      }
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

      &-buttons {
        & > a {
          display: inline-block;
          &:not(:first-child) {
            margin-top: 0;
            margin-left: 24px;
          }
        }
      }
    }

    &__info {
      padding: 16px 0;

      &-copyright {
        width: 190px;
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
  .footer__info-copyright {
    width: 210px;
  }
  .footer__social-buttons {
    & > a {
      display: block;
      text-align: start;

      &:not(:first-child) {
        margin-top: 12px;
        margin-left: 0;
      }
    }
  }
  address {
    letter-spacing: -1px;
  }
}
</style>
