class Bootloader extends Phaser.Scene {

    constructor() {
        super({ key: "Bootloader" });
    }

    preload() {
        this.load.on("complete", () => {
            this.scene.start("Scene_play");
        });

        this.load.image("ball", "./assets/circle.png");
        this.load.image("opponent", "./assets/tile.png");
        this.load.image("food", "./assets/food.png");
        this.load.image("background", "./assets/tile.png");

    }


}

export default Bootloader;