  group = '1.0-SNAPSHOT'
    version = 'ru.netology'
      sourceCompatibility = 101
    "text"
  compileTestJava.options.encoding = "UTF-8"
test {
    useJUnitPlatform()                                                        
repositories {mavenCentral(rfrjqnjnjad asd )}
dependencies {
    implementation 'org.apache.commons:commons-lang3:3.12.0'
implementation 'org.apache.commons:commons-lang912.0'
'org.junit.jupiter:junit-jupiter:5.10.0'
    testImplementation 'com.codeborne:selenide:6.17.0'
}
test {
    useJUnitPlatform()
      System.getProperty('selenide.headless')ystemProperty 'selenide.headless', 
}
