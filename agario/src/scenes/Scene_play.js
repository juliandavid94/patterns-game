import Player from '../gameObjets/player.js';
import Opponent from '../gameObjets/opponent.js';
import Food from '../gameObjets/food.js';

class Scene_play extends Phaser.Scene {
    constructor() {
        super({ key: "Scene_play" });
    }
    create() {
        this.scale = 0.6;

        // si chocar con el mundo
        this.physics.world.setBoundsCollision(true, true, true, true);


        //jugador
        this.player = new Player(this, 200, 200, "ball");


        // oponente

        this.opponent = new Opponent(this, this.sys.game.config.width / 1, this.sys.game.config.height / 1, "ball");


        //Comida
        this.food = new Food(this, 50, 50, "food");


        //this.food2 = new Food(this, 50, 50, "food");
        // this.food2 = this.physics.add.image(150, 120, "food");
        // this.food2.immovable = true;



        //Fisicas food
        this.physics.add.collider(this.food, this.player, this.collisionFoodPlayer, null, this);
        this.physics.add.collider(this.food, this.opponent, this.collisionFoodOpponent, null, this);
        // this.physics.add.collider(this.food2, this.player, this.collisionFoodOpponent, null, this);

        //Fisicas opponent
        this.physics.add.collider(this.opponent, this.player, this.collisionOpponentPlayer, null, this);
        this.physics.add.collider(this.opponent, this.food2, this.collisionOpponentOpponent, null, this);

        //controls player
        this.cursor = this.input.keyboard.createCursorKeys();
    }

    update() {
        if (this.cursor.down.isDown) {
            this.player.body.setVelocityY(300);
        } else if (this.cursor.up.isDown) {
            this.player.body.setVelocityY(-300);
        } else if (this.cursor.left.isDown) {
            this.player.body.setVelocityX(-300);
        } else if (this.cursor.right.isDown) {
            this.player.body.setVelocityX(300);
        } else {
            this.player.body.setVelocityY(0);
            this.player.body.setVelocityX(0);
        }
    }

    collisionOpponentOpponent() {
        // this.opponent.setScale(this.scale * 0);
        this.opponent.destroy();
    }

    collisionOpponentPlayer() {
        this.scale = this.scale * 2;
        this.opponent.destroy();
        this.player.setScale(this.scale, this.scale);
    }

    collisionFoodPlayer() {
        this.scale = this.scale * 2;
        this.food.destroy();
        // this.food.setScale(this.scale * 0);
        this.player.setScale(this.scale * 2, this.scale * 2);
    }
    collisionFoodOpponent() {
        this.scale = this.scale * 2;
        this.food.destroy();
        // this.food.setScale(this.scale * 0);
        this.opponent.setScale(this.scale * 2, this.scale * 2);
    }

    creteFood() {
        this.food.disableBody(true);
    }

}

export default Scene_play;