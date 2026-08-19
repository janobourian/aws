# ElastiCache

## Overview

Amazon ElastiCache is a web service that makes it easy to deploy, operate, and scale an in-memory cache in the cloud. It provides a high-performance, scalable, and cost-effective caching solution that can be used to improve the performance of applications by reducing the latency and load on databases.

* ElastiCache is to get managed Redis or Memcached
* Caches are in-memory databases with really high performance, low latency
* ElastiCache supports two open-source in-memory caching engines:
  * Redis: A popular in-memory data structure store that supports various data types and offers advanced features like replication, persistence, and pub/sub messaging.
  * Memcached: A high-performance, distributed memory object caching system that is simple and easy to use.
* Helps reduce load off of databases for read intensive workloads
* Helps make your application stateless
* Using ElastiCache involves heavy application code changes
* Process:
  * Application <-> Amazon ElastiCache
  * Application -> Cache miss
  * Application <-> Amazon RDS
  * Application -> Write to cache

* Redis is High Available
  * Replication
* Memchached is not High Available
  * Sharding

## Strategies

* Cache eviction can occur in three ways
  * You delete the item explicity in the cache
  * Item is evicted because the memory is full and it is not recently used
  * You set an item time-to-live
* If too many evictions happen due to memory, you should scale up or out

## Solution Architect Level

* Use case: User Session Store:
  * User logs into any of the application
  * The application writes the session data into ElastiCache
  * The user hits another instance of our application
  * The instance retrieves the data and the user is already logged in
