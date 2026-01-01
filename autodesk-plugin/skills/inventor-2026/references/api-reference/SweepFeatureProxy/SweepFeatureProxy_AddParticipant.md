# SweepFeatureProxy.AddParticipant Method

Parent Object: [SweepFeatureProxy](../SweepFeatureProxy/SweepFeatureProxy.md)

## Description

Add the specified occurrence from the list of participants for this feature. This method only applies to assembly features.

## Syntax

SweepFeatureProxy.**AddParticipant**( ***Occurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Occurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | Input ComponentOccurrence object that specifies the participant to be added. An error occurs if the input ComponentOccurrence is not a leaf occurrence. |

## Version

Introduced in version 2010
