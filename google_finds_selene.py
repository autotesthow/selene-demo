from selene import by, be, have
from selene.support.shared import browser


browser.open('https://google.com/ncr')
browser.element('[name=q]').type('selenidejs').press_enter()

browser.all('#rso>div').should(have.size(9))
browser.all('#rso>div').first.should(have.text('SelenideJS - GitHub'))
browser.all('#rso>div').first.element('h3').click()

browser.should(have.title_containing('GitHub - KnowledgeExpert/selenidejs'))
