"use strict";

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var swiper = new Swiper(".heroSwiper", _defineProperty({
  slidesPerView: 1,
  spaceBetween: 30,
  autoplay: {
    delay: 2000,
    disableOnInteraction: false
  }
}, "autoplay", {
  delay: 2500,
  disableOnInteraction: false
}));
var swiper = new Swiper(".flipSwiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  pagination: {
    el: ".swiper-pagination",
    clickable: true
  },
  autoplay: {
    delay: 1500,
    disableOnInteraction: false
  }
});
$('.mobilemenu').click(function (e) {
  e.preventDefault();
  $('.mobilebox').show('fast');
});
$('.cross_icon').click(function (e) {
  e.preventDefault();
  $('.mobilebox').hide('fast');
});
$('.tab-btn').click(function (e) {
  e.preventDefault();
  var dropdownContainer = $(this).next('.mobile-submenu');
  var isRotated = $(this).attr('style') === 'transform: rotate(180deg);';

  if (isRotated) {
    $(this).removeAttr('style');
  } else {
    $(this).attr('style', 'transform: rotate(180deg);');
  }

  if (dropdownContainer.is(':visible')) {
    dropdownContainer.slideUp('fast');
  } else {
    dropdownContainer.slideDown('fast');
  }
});
document.getElementById('dropdown').addEventListener('change', function () {
  var selectedOption = this.options[this.selectedIndex].text;
  this.previousElementSibling.innerText = selectedOption;
});
console.log("Welcome to Artist Page"); // Initialize the Variables

var songIndex = 0;
var audioElement = new Audio('assets/songs/1.mp3');
var masterPlay = document.getElementById('masterPlay');
var myProgressBar = document.getElementById('myProgressBar');
var gif = document.getElementById('gif');
var masterSongName = document.getElementById('masterSongName');
var songItems = Array.from(document.getElementsByClassName('songItem'));
var songs = [{
  songName: "Warriyo - Mortals [NCS Release]",
  filePath: "songs/1.mp3",
  coverPath: "covers/1.jpg"
}, {
  songName: "Cielo - Huma-Huma",
  filePath: "songs/2.mp3",
  coverPath: "covers/2.jpg"
}, {
  songName: "DEAF KEV - Invincible [NCS Release]-320k",
  filePath: "songs/3.mp3",
  coverPath: "covers/3.jpg"
}, {
  songName: "Different Heaven & EH!DE - My Heart [NCS Release]",
  filePath: "songs/4.mp3",
  coverPath: "covers/4.jpg"
}, {
  songName: "Janji-Heroes-Tonight-feat-Johnning-NCS-Release",
  filePath: "songs/5.mp3",
  coverPath: "covers/5.jpg"
}, {
  songName: "Rabba - Salam-e-Ishq",
  filePath: "songs/2.mp3",
  coverPath: "covers/6.jpg"
}, {
  songName: "Sakhiyaan - Salam-e-Ishq",
  filePath: "songs/2.mp3",
  coverPath: "covers/7.jpg"
}, {
  songName: "Bhula Dena - Salam-e-Ishq",
  filePath: "songs/2.mp3",
  coverPath: "covers/8.jpg"
}, {
  songName: "Tumhari Kasam - Salam-e-Ishq",
  filePath: "songs/2.mp3",
  coverPath: "covers/9.jpg"
}, {
  songName: "Na Jaana - Salam-e-Ishq",
  filePath: "songs/4.mp3",
  coverPath: "covers/10.jpg"
}];
songItems.forEach(function (element, i) {
  element.getElementsByTagName("img")[0].src = songs[i].coverPath;
  element.getElementsByClassName("songName")[0].innerText = songs[i].songName;
}); // Handle play/pause click

masterPlay.addEventListener('click', function () {
  if (audioElement.paused || audioElement.currentTime <= 0) {
    audioElement.play();
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');
    gif.style.opacity = 1;
  } else {
    audioElement.pause();
    masterPlay.classList.remove('fa-pause-circle');
    masterPlay.classList.add('fa-play-circle');
    gif.style.opacity = 0;
  }
}); // Listen to Events

audioElement.addEventListener('timeupdate', function () {
  // Update Seekbar
  progress = parseInt(audioElement.currentTime / audioElement.duration * 100);
  myProgressBar.value = progress;
});
myProgressBar.addEventListener('change', function () {
  audioElement.currentTime = myProgressBar.value * audioElement.duration / 100;
});

var makeAllPlays = function makeAllPlays() {
  Array.from(document.getElementsByClassName('songItemPlay')).forEach(function (element) {
    element.classList.remove('fa-pause-circle');
    element.classList.add('fa-play-circle');
  });
};

Array.from(document.getElementsByClassName('songItemPlay')).forEach(function (element) {
  element.addEventListener('click', function (e) {
    makeAllPlays();
    songIndex = parseInt(e.target.id);
    e.target.classList.remove('fa-play-circle');
    e.target.classList.add('fa-pause-circle');
    audioElement.src = "songs/".concat(songIndex + 1, ".mp3");
    masterSongName.innerText = songs[songIndex].songName;
    audioElement.currentTime = 0;
    audioElement.play();
    gif.style.opacity = 1;
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');
  });
});
document.getElementById('next').addEventListener('click', function () {
  if (songIndex >= 9) {
    songIndex = 0;
  } else {
    songIndex += 1;
  }

  audioElement.src = "songs/".concat(songIndex + 1, ".mp3");
  masterSongName.innerText = songs[songIndex].songName;
  audioElement.currentTime = 0;
  audioElement.play();
  masterPlay.classList.remove('fa-play-circle');
  masterPlay.classList.add('fa-pause-circle');
});
document.getElementById('previous').addEventListener('click', function () {
  if (songIndex <= 0) {
    songIndex = 0;
  } else {
    songIndex -= 1;
  }

  audioElement.src = "songs/".concat(songIndex + 1, ".mp3");
  masterSongName.innerText = songs[songIndex].songName;
  audioElement.currentTime = 0;
  audioElement.play();
  masterPlay.classList.remove('fa-play-circle');
  masterPlay.classList.add('fa-pause-circle');
});