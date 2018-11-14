import { Selector } from 'testcafe';

fixture ('verify all elements are present on page')
    .page ('http://devexpress.github.io/testcafe/example');

test ("verify header elements are visible", async t => {
    const header = Selector('header').child('h1');
    const subHeader = Selector('header').child('p');
    
    if (await header.exists && await header.visible)
        await t.expect(header.innerText).eql('Example', 'header contains text: Example' );
    
    if (await subHeader.exists && await subHeader.visible)   
        await t.expect(subHeader.innerText).eql('This webpage is used as a sample in TestCafe tutorials.', 'subheader contains text')
})

test("verify user can input text to input box", async t => {
    const nameBox = Selector('#developer-name');

    await t
        .expect(nameBox.innerText).eql('', "empty input")
        .typeText(nameBox, '1st try')
        .setNativeDialogHandler((type: "confirm", text: 'Reset information before proceeding?') => true)
        .click('#populate')
        .expect(nameBox.innerText).eql('', 'innerText')
        .typeText(nameBox, '2nd try')
        .setNativeDialogHandler((type: "confirm", text: 'Reset information before proceeding?') => false)
        .click('#populate')
   //     .expect(nameBox.innerText).eql('2nd try', 'innerText');
});
test ('verify submit button is disabled until user start typing', async t => {
    const submit = Selector ('#submit-button');

    await t
        .expect(submit.withAttribute('disabled', 'disabled'))
     
    await t
        .typeText('#developer-name', 'John Smith')
        .expect(submit).notEql({ disabled: 'disabled'}, "element doesnt contain attribute") 
        .click(submit);
    
    const articleHeader = Selector('.result-content').find('h1');

        // Obtain the text of the article header
    let articleHeaderText = articleHeader.innerText
        if (await articleHeader.visible && articleHeader.exists)
            await t.expect(articleHeaderText).eql('Thank you, John Smith!');

})
