# CHANGELOG



## v0.5.0 (2024-04-20)

### Feature

* feat: trigger milestone 4 release (#142)

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`277c082`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/277c082b1015f84b1bd857f170a68caa89bdf6dd))


## v0.4.0 (2024-04-20)

### Documentation

* docs: add geo-view description sentence (#140) ([`7b91e06`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/7b91e0644c81351169126521a54256dcbdf318d7))

* docs: update gif in README (#139)

* docs: update gif in README

* docs: improve the resolution of gif

* docs: improve the resolution

* docs: improve gif

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`9cedfff`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/9cedfffbf6f31671b56c52b5c4645356437a4f5f))

* docs: Create m4-reflection.md (#134)

* docs: Create m4-reflection.md

* docs: Add challenging part in the reflection

* Update the improvment points in Reflection

* docs: Update reflection

* docs: short notes for reflection

* docs: 500 wd count

* docs: minor fix of reflection

---------

Co-authored-by: shumlh &lt;tonyuglobe@gmail.com&gt;
Co-authored-by: Simon &lt;37085057+srfrew@users.noreply.github.com&gt;
Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`da8322e`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/da8322e402c2565258d59f90289c1a854a024aeb))

### Feature

* feat: Geo view (#135)

* feat: add geo plot

* feat: incorporate geo chart

python -m src.app

* feat: geo chart detail refine

* feat: geo chart refine

* feat: geo chart height change

* fix: conda env update

* fix: quick fix on the warnings with the toggle switch

* docs: added note of date range to clarify

* docs: added docstring to the new function

* docs: added missing packages in environment.yml

* build: add country geojson

* feat: geo-chart memoize, vectorize

* fix: country code parsing and geo-area loading notice

* fix: ui removed asterix, fixing location error

* fix: remove Fiji due to geo-dataset charting

* refactor: update geo date language

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt;
Co-authored-by: Simon Frew &lt;simon.r.frew@gmail.com&gt; ([`81ff472`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/81ff472a7e33b3a17452c88d2ee933dd3408208b))

* feat: Added tutorial (#136)

* feat: add tutorial for the dashboard

* feat: change the button position to sidebar

* feat: change button style

* docs: added the tutorial in the README as well

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt;
Co-authored-by: Celeste Zhao &lt;emilyxxzhao@outlook.com&gt; ([`3651ec4`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/3651ec4f73950ab9eb8163524514cc9202ac7600))

* feat: implement memoization for country data preprocessing, minor bugfixes (#133)

* fix: vectorize .apply in data.py

* refactor: remove unnecesary jsonify

* refactor: vectorize part of plotting.py

* feat: implement past-widget state

* feat: write widget state on app load

* fix: add widget_state to update_geo_area

* feat: update current widget state in charting functions

* feat: create compare_widget_states for commodities

* build: add jsonpickle

* feat: store prior commodity charts for reuse

* feat: reuse prior commodity charts, null selection warning

* fix: remove setting with copy warning

* build: add jsonpickle to pip

* refactor: change output to state in prior chart

* fix: remove accidentally commited improvements.ipynb

* refactor: disable debug mode

* refactor: update footers

* build: add flask_caching

* feat: performance:  flask_caching memoization for data loading / preprocessing

* fix: remove callback error in toggle switch ([`c473431`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/c473431412235f8c7bb891d87a8da4e6188e2b4f))

### Fix

* fix: revert erroneous commit to m1_EDA.ipynb (#141) ([`bd98313`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/bd983131b7539db5bd8d2ba24d659986a2959003))

* fix: performance: remove pd.apply in codebase (#126)

* fix: vectorize .apply in data.py

* refactor: remove unnecesary jsonify

* refactor: vectorize part of plotting.py ([`59ec8c0`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/59ec8c009f11516ae7a5dc44ad4031fbdb0538b4))

* fix: date-range &amp; country dropdowns

* fix: Sort country dropdown

* feat: change date selection from calendar to slicer

* fix: Update the update mode for date range slider ([`085574f`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/085574f7bdcaef21561e2b65268188d003e43f87))

* fix: match index / commodity chart width (#109) ([`6dc0d65`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/6dc0d65c9cb4cfb04022991c1120a381df93ff16))

### Unknown

* Update layout during country update (#137)

* fix: vectorize .apply in data.py

* refactor: remove unnecesary jsonify

* refactor: vectorize part of plotting.py

* feat: implement past-widget state

* feat: write widget state on app load

* fix: add widget_state to update_geo_area

* feat: update current widget state in charting functions

* feat: create compare_widget_states for commodities

* build: add jsonpickle

* feat: store prior commodity charts for reuse

* feat: reuse prior commodity charts, null selection warning

* fix: remove setting with copy warning

* build: add jsonpickle to pip

* refactor: change output to state in prior chart

* fix: remove accidentally commited improvements.ipynb

* refactor: disable debug mode

* refactor: update footers

* build: add flask_caching

* feat: performance:  flask_caching memoization for data loading / preprocessing

* fix: remove callback error in toggle switch

* fix: disable country selection removal

* fix: Freeze widgets when loading the data

* feat: Add Loading Data notice when loading the data

* fix: update docstring for function &#39;
reset_widget_values&#39;

* fix: Limit the prototype countries to 10

* fix: re-introduce the server = app.server to resolve the render.com error

---------

Co-authored-by: Simon Frew &lt;simon.r.frew@gmail.com&gt;
Co-authored-by: JohnShiuMK &lt;asbjchk@yahoo.com.hk&gt;
Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`89f4bbb`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/89f4bbbabcb0282f09d28691bdc3ec9119363b9f))

* Update docs (#123)

* docs: updated the installation guide, changed the ssh clone to http

* docs: removed the whitespace in front of the commends in the README

* fix: addressed the warning of plotting

* fix: resolved package mismatch issue

* fix: added glossary in footer to explain MoM and YoY

* feat: add favicon

* fix: correct the position of favicon

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`a4fed2f`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/a4fed2fca52ca6a791c00b1392a4ae8d8026224b))

* Update basic view (#118)

* fix: Sort country dropdown

* feat: change date selection from calendar to slicer ([`5aca900`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/5aca9003745e5f29bd6bf709f82c2a74a9d4885b))


## v0.3.0 (2024-04-14)

### Documentation

* docs: create m3_reflection.md (#89)

* docs: create m3_reflection.md

* docs: Update the m3-reflection.md

* Update m3-reflection.md

* Update m3-reflection.md

* Update m3-reflection.md

* docs: updated reflection

* Update m3-reflection.md

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`6774b6a`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/6774b6a7c8e2d0f2734b9576789b4d790902eeb0))

### Feature

* feat: trigger m3 release (#100)

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`18da174`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/18da174d0700a914009ddcbc7d769cb0fb48476a))

* feat: Add filter_major_data function for data filtering (#88)

* feat: Add filter_major_data function for data filtering

* fix: remove debug mode for deployment

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt;
Co-authored-by: JohnShiuMK &lt;asbjchk@yahoo.com.hk&gt; ([`e171647`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/e1716472706471c0a7851baa7781181a75cf56f4))

### Fix

* fix: added page title and distinguish the breakdown and the index (#90)

* fix: added page title and distinguish the breakdown and the index

* fix: the top and side navigation matching

* fix: the alignment of the small charts

* fix: the width of the small charts

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`cedbbfa`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/cedbbfade7300029fc2fc58c0f08512fe0436e39))

### Unknown

* 84 challenging milestone 3 geo chart (#99)

* refactor: create callbacks.py

* refactor: merge fetch_data.py, data_preprocess.py, and calc_index.py into data.py

* refactor: finalize code layout update

* feat: draft geo_area

* feat: implemented toggle switching for new charts

* bug: update sidebar, still wip

* feat: update sidebar layout

* fix: correct chart overflow &amp; scrolling

* docs: update challenging section for geo-chart refactor

* docs: corrected for consistency

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`f4cd07b`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/f4cd07bdc28298e273865c40c1b8bd7aaad56936))

* 75 5 break code into multiple files (#98)

* refactor: create callbacks.py

* refactor: merge fetch_data.py, data_preprocess.py, and calc_index.py into data.py

* refactor: finalize code layout update ([`827634c`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/827634cf91178d1d2ffa6d6546cc27a9433b3560))

* Aesthetics change (#97)

* Aesthetics change

* Align the marker and x axis tickvalues in the line charts ([`aa59b97`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/aa59b97cacd92aef19e13d483549244ce992e7cd))

* Update data preprocess (#96)

* fix: update the deduplication logic in function &#39;filter_major_data&#39;

* feat: Add function &#39;fill_missing_data&#39; to fillna ([`2645beb`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/2645bebe44e8d14899b10098d460fc2cba463b90))

* Aesthetics improve (#94)

* feat: add card

* feat: improve the aesthetics of the line charts

* feat: refine the aesthetics of sidebar

* Change heights

* Change layout

* Change figure chart

* Refine card

* Refine details

* Minor change on topbar ([`bd90a6f`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/bd90a6fee34e5420f878311f61046ebdd33d32e3))

* 62 bugfix chart render sync delay (#87)

* fix: sync chart plotting by merging callbacks

* refactor: lint code

* fix: remove variable ([`3fe3742`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/3fe3742cf96f294086181830ce98eeaa917f132b))


## v0.2.0 (2024-04-06)

### Documentation

* docs: modified the docstring of the functions (#67)

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`df7f05d`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/df7f05dc2a5ffd74f43aa147ff3adb2d1e322358))

* docs: create demo.gif (#70) ([`3796281`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/37962812652ff2bd5a829ad9fc0e293105302e67))

### Feature

* feat: trigger 0.2.0 release for milestone 2 submission (#72)

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`886271d`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/886271dfa1f1ea7f39419ad9f21ba260691dc6dc))

* feat: trigger 0.2.0 release for milestone 2 submission (#71)

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`d3cf708`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/d3cf708c26f680a4dbf4521b60f429ead7fe88ec))

* feat: Combine components (#57)

* feat: update plots in the commodities area

* fix: add empty init file for render.com deployment

* fix: correct app.py to collaborate with __init__

* feat: combine index to the dashboard

* docs: updated README on how we should start the app

* fix: refactored codes

* fix: fixed the bugs on date range selection and ratio of plots

* fix: the x-axis labels

* fix: modified the default start date

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`a160eb9`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/a160eb9b97ff69ffb700d746981206dab0d39691))

* feat: app initialization, data loading, widget initialization (#50)

* build: update env packages for pip / HDX / data processing

* feat: fetch_data.py for country dataset and data processing

* feat:  draft fetch_country_index_df()

* feat: implement fetch_country_data()

* refactor: set country_index_df index to country name

* feat:  complete fetch_data functions and lint

* build: update requirements.txt

* build: correct yml for pip dependencies

* feat: draft callback functions for data integration

* feat: draft update_country_data and implement dcc.Store

* refactor: update data outputs to json

* feat: draft update_widget_values

* refactor: test country data / widget functions

* fix: futureproof read_json with StringIO

* refactor: further testing for widget initialization

* fix: add default values to selections

* feat: frontend chart areas

---------

Co-authored-by: JohnShiuMK &lt;asbjchk@yahoo.com.hk&gt; ([`f16da0a`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/f16da0aff713d86600b418a6c02aaf2df58172d9))

* feat: implement data fetch and preprocessing (#49)

* build: update env packages for pip / HDX / data processing

* feat: fetch_data.py for country dataset and data processing

* feat:  draft fetch_country_index_df()

* feat: implement fetch_country_data()

* refactor: set country_index_df index to country name

* feat:  complete fetch_data functions and lint

* build: update requirements.txt

---------

Co-authored-by: JohnShiuMK &lt;asbjchk@yahoo.com.hk&gt; ([`d04fbb8`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/d04fbb8ba7b1eec858ad74c753247680578363fa))

* feat: Add food price index generator and figure chart generator funct… (#46)

* feat: Add food price index generator and figure chart generator functions

* fix: fix name in environment.yml

* feat: Build line chart feature (#48)

* feat: Add line chart for Food Price Index

Add function generate_line_chart_fpi()

* feat: Add line chart for selected commodities

Add function generate_line_chart_commodities()

---------

Co-authored-by: celestezhao &lt;143828198+celestezhao@users.noreply.github.com&gt;
Co-authored-by: Simon &lt;37085057+srfrew@users.noreply.github.com&gt; ([`c387724`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/c387724610338cc3a757c46be2c103d7a2c35d36))

### Fix

* fix: add empty init file for render.com deployment (#56)

* fix: add empty init file for render.com deployment

* fix: correct app.py to collaborate with __init__

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`e64919a`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/e64919ab4b13e7ac83a1cce0485ec09635c598bf))

* fix: env update (#54)

* fix: Update env .yml file

vegafusion=1.4.5 --&gt; vegafusion=1.6.6
vegafusion-jupyter=1.4.5 --&gt; vegafusion-jupyter=1.6.6
This is to fix the error &#34;The versions of the vegafusion and vegafusion-python-embed packages must match and must be version 1.5.0 or greater&#34;

vl-convert-python=1.1.0 --&gt; vl-convert-python=1.3.0
Required by Altair plotting

* fix: Update requirements.txt

---------

Co-authored-by: Celeste Zhao &lt;emilyxxzhao@outlook.com&gt; ([`52690c9`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/52690c9c9efd67b182d65a6d4e061c879c553edc))

* fix: Update env .yml file (#47)

vegafusion=1.4.5 --&gt; vegafusion=1.6.6
vegafusion-jupyter=1.4.5 --&gt; vegafusion-jupyter=1.6.6
This is to fix the error &#34;The versions of the vegafusion and vegafusion-python-embed packages must match and must be version 1.5.0 or greater&#34;

vl-convert-python=1.1.0 --&gt; vl-convert-python=1.3.0
Required by Altair plotting ([`2410123`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/24101235a48134c94526b81be4fc654331faa72d))

* fix: update the files to prepare for deployment (#44)

* fix: update the files to prepare for deployment

* fix: removed unnecessary packages in requirements.txt

* fix: fixed typo in requirements.txt

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`9fe99b4`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/9fe99b48dfe7d3b5a57e58f17e56a17730739b85))

### Unknown

* Draft reflection and update README (#68)

* docs: Draft m2-reflection.md

* docs: Update README.md

* docs: fix README.md

* fix: updated environment requirements to avoid warnings on start

* docs: updated link

* docs: corrected link in the README

* docs: create demo.gif

* docs: update logo

* docs: update attributions

* docs: include reference to demo.gif

* docs: minor fixes

* docs: m2 reflection edits

* docs: m2 reflection s3-s4 update

* docs: bring to below 500 words

* docs: attribution for data source

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt;
Co-authored-by: Simon Frew &lt;simon.r.frew@gmail.com&gt; ([`e32d013`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/e32d013cf5c62c40df72a9570d5435338f105b1c))

* Update footer (#66)

* fix: test html footer addition

* feat: Add footer to app.py ([`d26f678`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/d26f678b21add8cd7266ff976c6dafd68173eccb))

* Initialize dashboard (#34)

* app: init dashboard and update necessary packages

* docs: update installation guide

* fix: correct typo in environment.yml

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`3b22f1f`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/3b22f1fcd36f5315770f9362fb14f726f0aa5ba7))


## v0.1.0 (2024-03-30)

### Ci

* ci: remove cicd of the python-semantic-release thing, not working because of the branch protection (#19)

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`13aff80`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/13aff80bd7e027b83c0da61a2d15fc6055879f3a))

### Documentation

* docs: Condense and finalize M1 Proposal and README.md (#23)

* feat: added drafts of app sketch for section 4 in the proposal, to be discussed

* docs: shorten section 3 (1150 words)

* docs: refine section 1 in proposal.md and include purpose in README.md

* docs: refine s2 in m1_proposal.md

* docs: added section 4 app sketch description

* update sketches

* docs: added images into proposal section 4

* docs: added a white space under the image in section 4

* docs: removed the word checking warning, will convert it into a github issue

* docs: lint m1_proposal for markdown

* docs: condense s2 of m1_propsal

* docs: remove general public use case for word count in m1_proposal

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt;
Co-authored-by: shumlh &lt;tonyuglobe@gmail.com&gt;
Co-authored-by: Celeste Zhao &lt;emilyxxzhao@outlook.com&gt; ([`6f1dc11`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/6f1dc118c41793e3d358791dfdc33060a4c2c8bf))

* docs: (challenging) M1 EDA (#24) ([`7dfc3a4`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/7dfc3a43119b6b93c5ec4d54e2d8ba16c411ce21))

* docs: edit s2 in m1_proposal (#22)

* docs: populate m1_proposal.md

* docs: s3 from @tonyshumlh

* docs: add s1 from @tonyshumlh

* docs: lint m1_proposal for md

* docs: edit s1 in m1_propoal

* docs: edit s3 of m1_proposal

* docs: add general public user story to s3 in m1_proposal

* docs: spell-check for m1_proposal

* docs: edit s2 in m1_proposal

---------

Co-authored-by: Simon Frew &lt;simon.r.frew@gmail.com&gt;
Co-authored-by: JohnShiuMK &lt;asbjchk@yahoo.com.hk&gt; ([`495df23`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/495df232f4c6bbafad715797846e6d6ed1f54710))

* docs: draft complete for sections 1 and 3 of m1_proposal.md (#21)

* docs: populate m1_proposal.md

* docs: s3 from @tonyshumlh

* docs: add s1 from @tonyshumlh

* docs: lint m1_proposal for md

* docs: edit s1 in m1_propoal

* docs: edit s3 of m1_proposal

* docs: add general public user story to s3 in m1_proposal

* docs: spell-check for m1_proposal ([`691872f`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/691872f6e22f5cf28f891f455b087c2b90336aa9))

### Feature

* feat: Update ci-cd.yml (#30) ([`1166cfd`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/1166cfd0eb44d4ddd2d681912825c9d10b46d600))

* feat: Update ci-cd.yml for manual release trigger (#29) ([`af93748`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/af93748b7b996fcbe7ce064043576aa4aa70e7d4))

* feat: re-implement CI/CD with updated protections

This reverts commit 13aff80bd7e027b83c0da61a2d15fc6055879f3a.
Test CI/CD to reinstate ([`a92a316`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/a92a3168005e905d38ebfa5d976f60f792a92f51))

* feat: manually trigger release (#27)

Triggering release via CI/CD for Milestone 1 ([`9268da3`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/9268da3811db975dec83e05aea20e984e7f3efd4))

### Unknown

* Update repo structure (#6)

* docs: update repository structure to align milestone 1 requirement

* ci: added python-semantic-release github action for version number control

* docs: renamed file name to align milestone 1 requirement

* docs: added raw data for proposal section 2 and EDA

* fix: updated python version to 3.12 in ci-cd

* docs: added attributions for the templates

* docs: added CC-BY license to cover non-software content

* docs: corrected installation guide and license info in README

* docs: included some basic data wrangling, visualization, jupyter-related packages in the environment file

---------

Co-authored-by: John Shiu &lt;asbjchk.academic@gmail.com&gt; ([`b79386f`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/b79386f5cea3c14c5afcc3c90f55378ab953faec))

* Initial commit ([`a296c3f`](https://github.com/UBC-MDS/DSCI-532_2024_19_food-price-tracker/commit/a296c3fc836770f8d392bce979ccfe702d652a27))
