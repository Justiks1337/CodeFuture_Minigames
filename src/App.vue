<script setup>
import GameList from "@/components/Home/GameList.vue";
import Lheader from "@/components/layouts/Lheader.vue";
import Lfooter from "@/components/layouts/Lfooter.vue";
import ErrorPage from "@/components/ErrorPage/ErrorPage.vue";
</script>

<template>
  <Lheader />
  <GameList />
  <ErrorPage />
  <Lfooter />
</template>

<style lang="scss" scoped></style>
