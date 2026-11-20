# Back mini-OrigaMe — build multi-étapes (l'image finale ne contient ni Maven ni le code source)
# Phase C : épingler ces images par digest (@sha256:...) pour des builds reproductibles

FROM maven:3.9-eclipse-temurin-26 AS build
WORKDIR /src
COPY pom.xml .
RUN mvn -B -ntp dependency:go-offline
COPY src ./src
# Les tests sont déjà joués par la CI : on ne les relance pas dans l'image
RUN mvn -B -ntp package -DskipTests

FROM eclipse-temurin:8-jre
# Utilisateur non-root : si l'appli est compromise, l'attaquant n'est pas root dans le conteneur
RUN groupadd --system app && useradd --system --gid app app
WORKDIR /app
COPY --from=build /src/target/app.jar app.jar
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}
USER app
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
