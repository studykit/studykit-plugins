# MeasureTools.GetLoopLength Method

Parent Object: [MeasureTools](../MeasureTools/MeasureTools.md)

## Description

Method that returns the total length of a loop.

## Syntax

MeasureTools.**GetLoopLength**( ***Curves*** As Object ) As Double

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curves | Object | Object that specifies the loop. Valid inputs are:  * An Edge object * A 2d/3d sketch curve (SketchLine, SketchArc, etc.) (For the above inputs, the method returns the length of the loop that the input entity is a part of (whether open or closed). Based on the input, the method looks for a unique closed loop or a unique open loop (in that order). If one is found, the length is returned else the method returns an error.) * An ObjectCollection containing Edge objects or 2d/3d sketch curve objects. (The collection can contain all the elements of a loop or must contain enough number of elements to uniquely identify a loop. Else the method returns an error. Also, the input curves must be end to end connected and in order.) * An EdgeLoop object * A ProfilePath object * A ProfilePath3D object |

## Version

Introduced in version 11
