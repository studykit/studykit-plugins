# BalloonValueSets.Add Method

Parent Object: [BalloonValueSets](../BalloonValueSets/BalloonValueSets.md)

## Description

Method that creates a new BalloonValueSet.

## Remarks

The new created BalloonValueSet is returned. This is the equivalent of the 'Attach Balloon' and 'Attach Balloon From List' commands in the user interface.

## Syntax

BalloonValueSets.**Add**( ***Component*** As Object ) As [BalloonValueSet](../BalloonValueSet/BalloonValueSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Component | Object | Input object that defines the component that this balloon will be attached to. This can be one of the following: a ComponentOccurrence / ComponentOccurrenceProxy object, or a DrawingBOMRow object. |

## Version

Introduced in version 2009
