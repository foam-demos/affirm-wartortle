package com.affirm.checkout

import com.foam.opentelemetry.FoamInstrumentation
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean

@SpringBootApplication
class CheckoutServiceApplication {
    @Bean
    fun foamInstrumentation(): FoamInstrumentation {
        return FoamInstrumentation.builder()
            .serviceName("checkout-service")
            .apiKey(System.getenv("FOAM_API_KEY"))
            .isProduction(System.getenv("ENV") == "production")
            .build()
    }
}

fun main(args: Array<String>) {
    runApplication<CheckoutServiceApplication>(*args)
}