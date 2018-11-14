fixture `Login`
    .page `https://portal.accenture.com`;

const credentials = {
    email: "petra.zabojnikova@accenture.com",
    password: ""
};

test('Log in to page', async t => {
await t
    .wait(5000)
    .typeText('input[name="username"]', credentials.email)
    .typeText('input[name="password"]', credentials.password)
    .click('button[type="submit"]')
    .wait(60000)
});