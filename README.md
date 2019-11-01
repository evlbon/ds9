# With all nodes
![Image alt](https://github.com/laser4622/ds9/blob/master/Screenshot%202019-11-02%20at%2001.05.36.png)


rs0:SECONDARY> rs.status()
```
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T21:58:32.620Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572645509, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T21:58:29.293Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572645509, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T21:58:29.293Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572645509, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572645509, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T21:58:29.293Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T21:58:29.293Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572645508, 2),
	"lastStableCheckpointTimestamp" : Timestamp(1572645508, 2),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-11-01T21:58:27.353Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572645497, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T21:58:28.374Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T21:58:29.252Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "172.31.19.92:27017",
			"ip" : "172.31.19.92",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 162,
			"optime" : {
				"ts" : Timestamp(1572645509, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T21:58:29Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "could not find member to sync from",
			"electionTime" : Timestamp(1572645507, 1),
			"electionDate" : ISODate("2019-11-01T21:58:27Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "172.31.31.55:27017",
			"ip" : "172.31.31.55",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 15,
			"optime" : {
				"ts" : Timestamp(1572645509, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572645509, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T21:58:29Z"),
			"optimeDurableDate" : ISODate("2019-11-01T21:58:29Z"),
			"lastHeartbeat" : ISODate("2019-11-01T21:58:31.355Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T21:58:31.202Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "172.31.19.92:27017",
			"syncSourceHost" : "172.31.19.92:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 2,
			"name" : "172.31.30.13:27017",
			"ip" : "172.31.30.13",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 15,
			"optime" : {
				"ts" : Timestamp(1572645509, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572645509, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-11-01T21:58:29Z"),
			"optimeDurableDate" : ISODate("2019-11-01T21:58:29Z"),
			"lastHeartbeat" : ISODate("2019-11-01T21:58:31.356Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T21:58:31.212Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "172.31.19.92:27017",
			"syncSourceHost" : "172.31.19.92:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572645509, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572645509, 1)
}
```



rs0:PRIMARY> rs.config()
```
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "172.31.19.92:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "172.31.31.55:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "172.31.30.13:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbcaa794bc3f9382928fd85")
	}
}
```
# After drop primary node

![Image alt](https://github.com/laser4622/ds9/blob/master/Screenshot%202019-11-02%20at%2001.10.11.png)


rs0:PRIMARY> rs.status()
```
{
	"set" : "rs0",
	"date" : ISODate("2019-11-01T22:06:42.708Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572646002, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-11-01T22:06:42.006Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572646002, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-11-01T22:06:42.006Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572646002, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572646002, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-11-01T22:06:42.006Z"),
		"lastDurableWallTime" : ISODate("2019-11-01T22:06:42.006Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572645982, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572645982, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-11-01T22:06:01.463Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572645952, 3),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572645952, 3),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-11-01T22:06:02.001Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T22:06:03.008Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "172.31.19.92:27017",
			"ip" : "172.31.19.92",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-11-01T22:06:41.487Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T22:06:01.364Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to 172.31.19.92:27017 :: caused by :: Connection refused",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "172.31.31.55:27017",
			"ip" : "172.31.31.55",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 676,
			"optime" : {
				"ts" : Timestamp(1572646002, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T22:06:42Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572645961, 1),
			"electionDate" : ISODate("2019-11-01T22:06:01Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 2,
			"name" : "172.31.30.13:27017",
			"ip" : "172.31.30.13",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 504,
			"optime" : {
				"ts" : Timestamp(1572645992, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572645992, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-11-01T22:06:32Z"),
			"optimeDurableDate" : ISODate("2019-11-01T22:06:32Z"),
			"lastHeartbeat" : ISODate("2019-11-01T22:06:41.475Z"),
			"lastHeartbeatRecv" : ISODate("2019-11-01T22:06:41.004Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "172.31.31.55:27017",
			"syncSourceHost" : "172.31.31.55:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572646002, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572646002, 1)
}
```



rs0:PRIMARY> rs.config()
```
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "172.31.19.92:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "172.31.31.55:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 2,
			"host" : "172.31.30.13:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {

			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {

		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("5dbcaa794bc3f9382928fd85")
	}
}
```
