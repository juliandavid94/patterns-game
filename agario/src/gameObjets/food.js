class Food extends Phaser.GameObjects.Sprite {

    constructor(scene, x, y, type) {
        super(scene, x, y, type);
        scene.add.existing(this);
        scene.physics.world.enable(this);
        this.body.setCollideWorldBounds(true);
        this.body.setBounce(1);
        this.body.setVelocityX(-180);

        this.body.setVelocityY(Phaser.Math.Between(-120, 120));
    }
}

export default Food;