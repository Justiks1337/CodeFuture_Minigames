<script setup>
import GameList from "@/components/Home/GameList.vue";
import Lheader from "@/components/layouts/Lheader.vue";
import Lfooter from "@/components/layouts/Lfooter.vue";
import ErrorPage from "@/components/ErrorPage/ErrorPage.vue";
import LoadingPage from "@/components/Loading/LoadingPage.vue";
</script>

<template>
  <Lheader />
  <GameList />
  <ErrorPage />
  <LoadingPage />
  <Lfooter />
</template>

<style lang="scss"></style>
