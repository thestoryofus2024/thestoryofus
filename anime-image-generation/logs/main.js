const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');
const https = require('https');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    const url = process.argv[2];
    console.log(url)
    // Navigate to the site
    await page.goto(url, { waitUntil: 'networkidle0' });

    // Get all image URLs
    const imageUrls = await page.evaluate(() =>
        Array.from(document.images, img => img.src)
    );

    // Create a folder to save images
    const downloadFolder = './images';
    if (!fs.existsSync(downloadFolder)) {
        fs.mkdirSync(downloadFolder);
    }

    // Download each image
    for (const url of imageUrls) {
        const imageName = path.basename(url);
        const filePath = path.resolve(downloadFolder, imageName);

        const file = fs.createWriteStream(filePath);
        https.get(url, response => {
            response.pipe(file);
            file.on('finish', () => {
                file.close();
                console.log(`Downloaded: ${imageName}`);
            });
        });
    }

    await browser.close();
})();

