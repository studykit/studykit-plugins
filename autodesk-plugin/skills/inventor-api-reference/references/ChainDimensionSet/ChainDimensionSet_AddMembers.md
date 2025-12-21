# ChainDimensionSet.AddMembers Method

Parent Object: [ChainDimensionSet](../ChainDimensionSet/ChainDimensionSet.md)

## Description

Method that adds member(s) to the chain set based on the input geometry or dimension and returns the newly created member(s).

## Remarks

Following are the behaviors based on the input object:

GeometryIntent object - In this case 0, 1 or 2 new members can be added to the set based on the position and orientation of the selected geometry. The number of members created is equal to the number of point intents specified by the input GeometryIntent that are currently not in use by this chain dimension set. For example, if the GeometryIntent specifies a (currently unused) point intent, a single member is created. If the GeometryIntent specifies an edge, and both the end points are currently unused, two members are created.

An existing LinearGeneralDimension object - The specified linear dimension is deleted and the geometries that were attached to the linear dimension are used to create members within this set.

An existing ChainDimensionSet object - The specified chain dimension set is deleted and the geometries that were attached to the chain dimension set are used to create members within this set.

## Syntax

ChainDimensionSet.**AddMembers**( ***DimensionOrGeometry*** As Object ) As [GeneralDimensionsEnumerator](../GeneralDimensionsEnumerator/GeneralDimensionsEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| DimensionOrGeometry | Object | Input object that specifies the dimension or geometry used to define the chain dimension member(s). Valid input objects are GeometryIntent, LinearGeneralDimension and ChainDimensionSet. |

## Version

Introduced in version 2011
