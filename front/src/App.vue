<script setup>
import Lheader from "@/components/layouts/Lheader.vue";
import Lfooter from "@/components/layouts/Lfooter.vue";

import { useRouter } from "vue-router";
const router = useRouter();

import { useToken } from "./use/useToken";
const { getToken, setToken } = useToken();
const urlParams = new URL(window.location);
setToken(urlParams.search.slice(1));

import { getRouterUrls } from "./use/useGamesNames";
const routerUrls = getRouterUrls();

for (const el in routerUrls) {
  router.addRoute({
    path: `/queue/${el}`,
    name: `loading-${el}`,
    component: () => import("@/components/Loading/LoadingPage.vue"),
  });
}
</script>

<template>
  <Lheader />
  <RouterView />
  <Lfooter />
</template>

<style lang="scss"></style>
