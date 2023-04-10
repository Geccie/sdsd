/*************** 
 * Change Test *
 ***************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.5.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'change';  // from the Builder filename that created this script
let expInfo = {
    'participant': '01',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(insRoutineBegin());
flowScheduler.add(insRoutineEachFrame());
flowScheduler.add(insRoutineEnd());
flowScheduler.add(attentionRoutineBegin());
flowScheduler.add(attentionRoutineEachFrame());
flowScheduler.add(attentionRoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(endRoutineBegin());
flowScheduler.add(endRoutineEachFrame());
flowScheduler.add(endRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': '../6 стимулов/разные/4/4.2.png', 'path': '../6 стимулов/разные/4/4.2.png'},
    {'name': '../4 квадрата/разные/8/8.1.png', 'path': '../4 квадрата/разные/8/8.1.png'},
    {'name': '../6 стимулов/одинаковые/2.png', 'path': '../6 стимулов/одинаковые/2.png'},
    {'name': '../пять квадратов/разные/3/3.2.png', 'path': '../пять квадратов/разные/3/3.2.png'},
    {'name': '../6 стимулов/одинаковые/9.png', 'path': '../6 стимулов/одинаковые/9.png'},
    {'name': '../4 квадрата/разные/9/9.2.png', 'path': '../4 квадрата/разные/9/9.2.png'},
    {'name': '../пять квадратов/разные/9/9.1.png', 'path': '../пять квадратов/разные/9/9.1.png'},
    {'name': '../7 стимулов/разные/6/6.1.png', 'path': '../7 стимулов/разные/6/6.1.png'},
    {'name': '../4 квадрата/разные/10/10.2.png', 'path': '../4 квадрата/разные/10/10.2.png'},
    {'name': '../4 квадрата/разные/1/1.1.png', 'path': '../4 квадрата/разные/1/1.1.png'},
    {'name': '../7 стимулов/одинаковые/4.png', 'path': '../7 стимулов/одинаковые/4.png'},
    {'name': '../7 стимулов/разные/4/4.2.png', 'path': '../7 стимулов/разные/4/4.2.png'},
    {'name': '../4 квадрата/одинаковые/9.png', 'path': '../4 квадрата/одинаковые/9.png'},
    {'name': '../6 стимулов/разные/10/10.1.png', 'path': '../6 стимулов/разные/10/10.1.png'},
    {'name': '../пять квадратов/разные/9/9.2.png', 'path': '../пять квадратов/разные/9/9.2.png'},
    {'name': '../пять квадратов/разные/2/2.1.png', 'path': '../пять квадратов/разные/2/2.1.png'},
    {'name': '../4 квадрата/разные/8/8.2.png', 'path': '../4 квадрата/разные/8/8.2.png'},
    {'name': '../7 стимулов/одинаковые/8.png', 'path': '../7 стимулов/одинаковые/8.png'},
    {'name': '../пять квадратов/одинаковые/3.png', 'path': '../пять квадратов/одинаковые/3.png'},
    {'name': '../7 стимулов/разные/2/2.1.png', 'path': '../7 стимулов/разные/2/2.1.png'},
    {'name': '../пять квадратов/одинаковые/6.png', 'path': '../пять квадратов/одинаковые/6.png'},
    {'name': '../пять квадратов/одинаковые/8.png', 'path': '../пять квадратов/одинаковые/8.png'},
    {'name': '../6 стимулов/разные/8/8.2.png', 'path': '../6 стимулов/разные/8/8.2.png'},
    {'name': '../пять квадратов/разные/5/5.2.png', 'path': '../пять квадратов/разные/5/5.2.png'},
    {'name': '../7 стимулов/одинаковые/1.png', 'path': '../7 стимулов/одинаковые/1.png'},
    {'name': '../7 стимулов/разные/8/8.2.png', 'path': '../7 стимулов/разные/8/8.2.png'},
    {'name': '../пять квадратов/разные/1/1.1.png', 'path': '../пять квадратов/разные/1/1.1.png'},
    {'name': '../6 стимулов/разные/3/3.1.png', 'path': '../6 стимулов/разные/3/3.1.png'},
    {'name': '../пять квадратов/разные/8/8.2.png', 'path': '../пять квадратов/разные/8/8.2.png'},
    {'name': '../4 квадрата/разные/5/5.2.png', 'path': '../4 квадрата/разные/5/5.2.png'},
    {'name': '../6 стимулов/разные/4/4.1.png', 'path': '../6 стимулов/разные/4/4.1.png'},
    {'name': '../7 стимулов/разные/7/7.2.png', 'path': '../7 стимулов/разные/7/7.2.png'},
    {'name': '../6 стимулов/разные/7/7.2.png', 'path': '../6 стимулов/разные/7/7.2.png'},
    {'name': '../4 квадрата/разные/3/3.1.png', 'path': '../4 квадрата/разные/3/3.1.png'},
    {'name': '../6 стимулов/разные/7/7.1.png', 'path': '../6 стимулов/разные/7/7.1.png'},
    {'name': '../7 стимулов/разные/10/10.1.png', 'path': '../7 стимулов/разные/10/10.1.png'},
    {'name': '../square.xlsx', 'path': '../square.xlsx'},
    {'name': '../4 квадрата/одинаковые/8.png', 'path': '../4 квадрата/одинаковые/8.png'},
    {'name': '../пять квадратов/одинаковые/2.png', 'path': '../пять квадратов/одинаковые/2.png'},
    {'name': '../7 стимулов/разные/3/3.1.png', 'path': '../7 стимулов/разные/3/3.1.png'},
    {'name': '../4 квадрата/одинаковые/6.png', 'path': '../4 квадрата/одинаковые/6.png'},
    {'name': '../4 квадрата/разные/7/7.1.png', 'path': '../4 квадрата/разные/7/7.1.png'},
    {'name': '../6 стимулов/одинаковые/1.png', 'path': '../6 стимулов/одинаковые/1.png'},
    {'name': '../пять квадратов/разные/4/4.2.png', 'path': '../пять квадратов/разные/4/4.2.png'},
    {'name': '../4 квадрата/разные/1/1.2.png', 'path': '../4 квадрата/разные/1/1.2.png'},
    {'name': '../7 стимулов/разные/7/7.1.png', 'path': '../7 стимулов/разные/7/7.1.png'},
    {'name': '../4 квадрата/разные/6/6.2.png', 'path': '../4 квадрата/разные/6/6.2.png'},
    {'name': '../6 стимулов/одинаковые/3.png', 'path': '../6 стимулов/одинаковые/3.png'},
    {'name': '../7 стимулов/одинаковые/5.png', 'path': '../7 стимулов/одинаковые/5.png'},
    {'name': '../4 квадрата/разные/4/4.1.png', 'path': '../4 квадрата/разные/4/4.1.png'},
    {'name': '../4 квадрата/одинаковые/3.png', 'path': '../4 квадрата/одинаковые/3.png'},
    {'name': '../4 квадрата/разные/7/7.2.png', 'path': '../4 квадрата/разные/7/7.2.png'},
    {'name': '../6 стимулов/разные/2/2.2.png', 'path': '../6 стимулов/разные/2/2.2.png'},
    {'name': '../пять квадратов/одинаковые/9.png', 'path': '../пять квадратов/одинаковые/9.png'},
    {'name': '../4 квадрата/одинаковые/2.png', 'path': '../4 квадрата/одинаковые/2.png'},
    {'name': '../4 квадрата/разные/3/3.2.png', 'path': '../4 квадрата/разные/3/3.2.png'},
    {'name': '../6 стимулов/разные/2/2.1.png', 'path': '../6 стимулов/разные/2/2.1.png'},
    {'name': '../6 стимулов/разные/10/10.2.png', 'path': '../6 стимулов/разные/10/10.2.png'},
    {'name': '../7 стимулов/разные/9/9.2.png', 'path': '../7 стимулов/разные/9/9.2.png'},
    {'name': '../6 стимулов/одинаковые/5.png', 'path': '../6 стимулов/одинаковые/5.png'},
    {'name': '../4 квадрата/разные/4/4.2.png', 'path': '../4 квадрата/разные/4/4.2.png'},
    {'name': '../7 стимулов/одинаковые/6.png', 'path': '../7 стимулов/одинаковые/6.png'},
    {'name': '../7 стимулов/одинаковые/9.png', 'path': '../7 стимулов/одинаковые/9.png'},
    {'name': '../7 стимулов/разные/5/5.2.png', 'path': '../7 стимулов/разные/5/5.2.png'},
    {'name': '../7 стимулов/разные/3/3.2.png', 'path': '../7 стимулов/разные/3/3.2.png'},
    {'name': '../6 стимулов/разные/8/8.1.png', 'path': '../6 стимулов/разные/8/8.1.png'},
    {'name': '../пять квадратов/разные/8/8.1.png', 'path': '../пять квадратов/разные/8/8.1.png'},
    {'name': '../4 квадрата/одинаковые/7.png', 'path': '../4 квадрата/одинаковые/7.png'},
    {'name': '../4 квадрата/разные/2/2.2.png', 'path': '../4 квадрата/разные/2/2.2.png'},
    {'name': '../7 стимулов/разные/9/9.1.png', 'path': '../7 стимулов/разные/9/9.1.png'},
    {'name': '../пять квадратов/разные/3/3.1.png', 'path': '../пять квадратов/разные/3/3.1.png'},
    {'name': '../6 стимулов/одинаковые/6.png', 'path': '../6 стимулов/одинаковые/6.png'},
    {'name': '../пять квадратов/разные/1/1.2.png', 'path': '../пять квадратов/разные/1/1.2.png'},
    {'name': '../6 стимулов/разные/9/9.1.png', 'path': '../6 стимулов/разные/9/9.1.png'},
    {'name': '../7 стимулов/одинаковые/3.png', 'path': '../7 стимулов/одинаковые/3.png'},
    {'name': '../пять квадратов/разные/4/4.1.png', 'path': '../пять квадратов/разные/4/4.1.png'},
    {'name': '../пять квадратов/разные/6/6.1.png', 'path': '../пять квадратов/разные/6/6.1.png'},
    {'name': '../6 стимулов/разные/5/5.2.png', 'path': '../6 стимулов/разные/5/5.2.png'},
    {'name': '../7 стимулов/разные/1/1.2.png', 'path': '../7 стимулов/разные/1/1.2.png'},
    {'name': '../6 стимулов/одинаковые/7.png', 'path': '../6 стимулов/одинаковые/7.png'},
    {'name': '../7 стимулов/одинаковые/10.png', 'path': '../7 стимулов/одинаковые/10.png'},
    {'name': '../7 стимулов/разные/8/8.1.png', 'path': '../7 стимулов/разные/8/8.1.png'},
    {'name': '../4 квадрата/одинаковые/1.png', 'path': '../4 квадрата/одинаковые/1.png'},
    {'name': '../7 стимулов/разные/10/10.2.png', 'path': '../7 стимулов/разные/10/10.2.png'},
    {'name': '../пять квадратов/разные/6/6.2.png', 'path': '../пять квадратов/разные/6/6.2.png'},
    {'name': '../6 стимулов/разные/5/5.1.png', 'path': '../6 стимулов/разные/5/5.1.png'},
    {'name': '../6 стимулов/разные/1/1.1.png', 'path': '../6 стимулов/разные/1/1.1.png'},
    {'name': '../пять квадратов/разные/10/10.2.png', 'path': '../пять квадратов/разные/10/10.2.png'},
    {'name': '../пять квадратов/одинаковые/1.png', 'path': '../пять квадратов/одинаковые/1.png'},
    {'name': '../4 квадрата/разные/2/2.1.png', 'path': '../4 квадрата/разные/2/2.1.png'},
    {'name': '../пять квадратов/одинаковые/7.png', 'path': '../пять квадратов/одинаковые/7.png'},
    {'name': '../6 стимулов/разные/9/9.2.png', 'path': '../6 стимулов/разные/9/9.2.png'},
    {'name': '../пять квадратов/разные/7/7.1.png', 'path': '../пять квадратов/разные/7/7.1.png'},
    {'name': '../7 стимулов/разные/6/6.2.png', 'path': '../7 стимулов/разные/6/6.2.png'},
    {'name': '../4 квадрата/одинаковые/5.png', 'path': '../4 квадрата/одинаковые/5.png'},
    {'name': '../пять квадратов/разные/7/7.2.png', 'path': '../пять квадратов/разные/7/7.2.png'},
    {'name': '../4 квадрата/разные/9/9.1.png', 'path': '../4 квадрата/разные/9/9.1.png'},
    {'name': '../7 стимулов/разные/2/2.2.png', 'path': '../7 стимулов/разные/2/2.2.png'},
    {'name': '../пять квадратов/разные/5/5.1.png', 'path': '../пять квадратов/разные/5/5.1.png'},
    {'name': '../4 квадрата/разные/5/5.1.png', 'path': '../4 квадрата/разные/5/5.1.png'},
    {'name': '../7 стимулов/разные/1/1.1.png', 'path': '../7 стимулов/разные/1/1.1.png'},
    {'name': '../6 стимулов/одинаковые/8.png', 'path': '../6 стимулов/одинаковые/8.png'},
    {'name': '../7 стимулов/одинаковые/2.png', 'path': '../7 стимулов/одинаковые/2.png'},
    {'name': '../пять квадратов/одинаковые/10.png', 'path': '../пять квадратов/одинаковые/10.png'},
    {'name': '../4 квадрата/одинаковые/4.png', 'path': '../4 квадрата/одинаковые/4.png'},
    {'name': '../4 квадрата/одинаковые/10.png', 'path': '../4 квадрата/одинаковые/10.png'},
    {'name': '../6 стимулов/одинаковые/10.png', 'path': '../6 стимулов/одинаковые/10.png'},
    {'name': '../пять квадратов/одинаковые/4.png', 'path': '../пять квадратов/одинаковые/4.png'},
    {'name': '../4 квадрата/разные/10/10.1.png', 'path': '../4 квадрата/разные/10/10.1.png'},
    {'name': '../6 стимулов/разные/6/6.2.png', 'path': '../6 стимулов/разные/6/6.2.png'},
    {'name': '../7 стимулов/одинаковые/7.png', 'path': '../7 стимулов/одинаковые/7.png'},
    {'name': '../7 стимулов/разные/5/5.1.png', 'path': '../7 стимулов/разные/5/5.1.png'},
    {'name': '../6 стимулов/разные/1/1.2.png', 'path': '../6 стимулов/разные/1/1.2.png'},
    {'name': '../пять квадратов/разные/10/10.1.png', 'path': '../пять квадратов/разные/10/10.1.png'},
    {'name': '../6 стимулов/одинаковые/4.png', 'path': '../6 стимулов/одинаковые/4.png'},
    {'name': '../7 стимулов/разные/4/4.1.png', 'path': '../7 стимулов/разные/4/4.1.png'},
    {'name': '../6 стимулов/разные/6/6.1.png', 'path': '../6 стимулов/разные/6/6.1.png'},
    {'name': '../6 стимулов/разные/3/3.2.png', 'path': '../6 стимулов/разные/3/3.2.png'},
    {'name': '../4 квадрата/разные/6/6.1.png', 'path': '../4 квадрата/разные/6/6.1.png'},
    {'name': '../пять квадратов/разные/2/2.2.png', 'path': '../пять квадратов/разные/2/2.2.png'},
    {'name': '../пять квадратов/одинаковые/5.png', 'path': '../пять квадратов/одинаковые/5.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var insClock;
var instruction;
var key_resp2;
var attentionClock;
var text;
var square11Clock;
var squaressss;
var pauseClock;
var text_2;
var square12Clock;
var sqqr;
var questionClock;
var text_4;
var key_resp;
var restClock;
var text_8;
var key_resp_5;
var endClock;
var text_3;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "ins"
  insClock = new util.Clock();
  instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction',
    text: 'Здравствуйте! Мы заранее благодарим Вас за принятие участие в нашем исследовании. Сейчас Вам будут представлены изображения с квадратами разных цветов в разных количествах. \nЕсли цвета всех квадратов на первом изображении совпадают \nс цветами всех квадратов на втором, то нажмите стрелочку "вправо",\nиначе - "влево"\nБудьте внимательны!\nКак будете готовы приступить - нажмите "пробел".',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "attention"
  attentionClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Приготовьтесь!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "square11"
  square11Clock = new util.Clock();
  squaressss = new visual.ImageStim({
    win : psychoJS.window,
    name : 'squaressss', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.75, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "pause"
  pauseClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "square12"
  square12Clock = new util.Clock();
  sqqr = new visual.ImageStim({
    win : psychoJS.window,
    name : 'sqqr', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.75, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "question"
  questionClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'Если Вы считаете, что цвет всех квадратов на обоих изображениях был:\nОдинаковым - нажмите стрелку "вправо".\nРазным - нажмите стрелку "влево".',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'Да Вы просто супер-молодец!\nВы уже прошли 50% теста!\n\nПродолжайте в том же духе!\n(нажмите "пробел", как будете готовы продолжить)',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Аплодисменты!\nВы прошли весь тест!!!\nУра-ура-ура!\nОбязательно похвалите себя за проделанную работу!\n\nВы очень нам помогли :)\nСпасибо за участие! ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp2_allKeys;
var insComponents;
function insRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ins' ---
    t = 0;
    insClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp2.keys = undefined;
    key_resp2.rt = undefined;
    _key_resp2_allKeys = [];
    // keep track of which components have finished
    insComponents = [];
    insComponents.push(instruction);
    insComponents.push(key_resp2);
    
    for (const thisComponent of insComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function insRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ins' ---
    // get current time
    t = insClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instruction* updates
    if (t >= 0.0 && instruction.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction.tStart = t;  // (not accounting for frame time here)
      instruction.frameNStart = frameN;  // exact frame index
      
      instruction.setAutoDraw(true);
    }

    
    // *key_resp2* updates
    if (t >= 0.0 && key_resp2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp2.tStart = t;  // (not accounting for frame time here)
      key_resp2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp2.clearEvents(); });
    }

    if (key_resp2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp2_allKeys = _key_resp2_allKeys.concat(theseKeys);
      if (_key_resp2_allKeys.length > 0) {
        key_resp2.keys = _key_resp2_allKeys[_key_resp2_allKeys.length - 1].name;  // just the last key pressed
        key_resp2.rt = _key_resp2_allKeys[_key_resp2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of insComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function insRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ins' ---
    for (const thisComponent of insComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp2.corr, level);
    }
    psychoJS.experiment.addData('key_resp2.keys', key_resp2.keys);
    if (typeof key_resp2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp2.rt', key_resp2.rt);
        routineTimer.reset();
        }
    
    key_resp2.stop();
    // the Routine "ins" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var attentionComponents;
function attentionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'attention' ---
    t = 0;
    attentionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    attentionComponents = [];
    attentionComponents.push(text);
    
    for (const thisComponent of attentionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function attentionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'attention' ---
    // get current time
    t = attentionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of attentionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function attentionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'attention' ---
    for (const thisComponent of attentionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'C:/Users/evgen/OneDrive/Рабочий стол/square.xlsx',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(square11RoutineBegin(snapshot));
      trials_3LoopScheduler.add(square11RoutineEachFrame());
      trials_3LoopScheduler.add(square11RoutineEnd(snapshot));
      trials_3LoopScheduler.add(pauseRoutineBegin(snapshot));
      trials_3LoopScheduler.add(pauseRoutineEachFrame());
      trials_3LoopScheduler.add(pauseRoutineEnd(snapshot));
      trials_3LoopScheduler.add(square12RoutineBegin(snapshot));
      trials_3LoopScheduler.add(square12RoutineEachFrame());
      trials_3LoopScheduler.add(square12RoutineEnd(snapshot));
      trials_3LoopScheduler.add(questionRoutineBegin(snapshot));
      trials_3LoopScheduler.add(questionRoutineEachFrame());
      trials_3LoopScheduler.add(questionRoutineEnd(snapshot));
      trials_3LoopScheduler.add(restRoutineBegin(snapshot));
      trials_3LoopScheduler.add(restRoutineEachFrame());
      trials_3LoopScheduler.add(restRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var square11Components;
function square11RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'square11' ---
    t = 0;
    square11Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    squaressss.setImage(pic1);
    // keep track of which components have finished
    square11Components = [];
    square11Components.push(squaressss);
    
    for (const thisComponent of square11Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function square11RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'square11' ---
    // get current time
    t = square11Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *squaressss* updates
    if (t >= 0.0 && squaressss.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      squaressss.tStart = t;  // (not accounting for frame time here)
      squaressss.frameNStart = frameN;  // exact frame index
      
      squaressss.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (squaressss.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      squaressss.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of square11Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function square11RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'square11' ---
    for (const thisComponent of square11Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var pauseComponents;
function pauseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'pause' ---
    t = 0;
    pauseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    pauseComponents = [];
    pauseComponents.push(text_2);
    
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function pauseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'pause' ---
    // get current time
    t = pauseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of pauseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function pauseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'pause' ---
    for (const thisComponent of pauseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var square12Components;
function square12RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'square12' ---
    t = 0;
    square12Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    sqqr.setImage(pic2);
    // keep track of which components have finished
    square12Components = [];
    square12Components.push(sqqr);
    
    for (const thisComponent of square12Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function square12RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'square12' ---
    // get current time
    t = square12Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *sqqr* updates
    if (t >= 0.0 && sqqr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sqqr.tStart = t;  // (not accounting for frame time here)
      sqqr.frameNStart = frameN;  // exact frame index
      
      sqqr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sqqr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      sqqr.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of square12Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function square12RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'square12' ---
    for (const thisComponent of square12Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var questionComponents;
function questionRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'question' ---
    t = 0;
    questionClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    questionComponents = [];
    questionComponents.push(text_4);
    questionComponents.push(key_resp);
    
    for (const thisComponent of questionComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function questionRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'question' ---
    // get current time
    t = questionClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == key) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of questionComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function questionRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'question' ---
    for (const thisComponent of questionComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(key)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_5_allKeys;
var restComponents;
function restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rest' ---
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // Run 'Begin Routine' code from code
    if ((((trials_3.thisN + 1) % 40) !== 0)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(text_8);
    restComponents.push(key_resp_5);
    
    for (const thisComponent of restComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function restRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rest' ---
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of restComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rest' ---
    for (const thisComponent of restComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text_3);
    
    for (const thisComponent of endComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    for (const thisComponent of endComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
