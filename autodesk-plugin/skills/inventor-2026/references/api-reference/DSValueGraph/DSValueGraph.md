# DSValueGraph Object

## Description

The DSValueGraph object represents the graph that defines a value at various time steps.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetSegmentInterpolationType](../DSValueGraph/DSValueGraph_GetSegmentInterpolationType.md) | Method that returns the interpolation method used for the specified curve segment. A curve segment is defined as the curve between two of the value points. There are PointCount-1 segments. |
| [GetValueArray](../DSValueGraph/DSValueGraph_GetValueArray.md) | Gets the values in the graph. The array consists of time-value pairs. The unit type of the value will vary depending on the type of value this result represents. |
| [SetSegmentInterpolationType](../DSValueGraph/DSValueGraph_SetSegmentInterpolationType.md) | Sets the interpolation method used for the specified curve segment. A curve segment is defined as the curve between two of the value points. There are PointCount-1 segments. |
| [SetValueUsingArray](../DSValueGraph/DSValueGraph_SetValueUsingArray.md) | Sets the values in the graph. The array consists of time-value pairs. The unit type of the value will vary depending on the type of value this result represents. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DSValueGraph/DSValueGraph_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [PointCount](../DSValueGraph/DSValueGraph_PointCount.md) | Gets the number of points in the graph. |
| [Type](../DSValueGraph/DSValueGraph_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DSValue.Graph](../DSValue/DSValue_Graph.md)

## Version

Introduced in version 2013
