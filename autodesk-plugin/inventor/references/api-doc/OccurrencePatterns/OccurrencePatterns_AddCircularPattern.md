# OccurrencePatterns.AddCircularPattern Method

Parent Object: [OccurrencePatterns](../OccurrencePatterns/OccurrencePatterns.md)

## Description

Method that creates a new circular occurrence pattern of input component(s).

## Syntax

OccurrencePatterns.**AddCircularPattern**( ***ParentComponents*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***AxisEntity*** As Object, ***AxisEntityNaturalDirection*** As Boolean, ***AngleOffset*** As Variant, ***Count*** As Variant ) As [CircularOccurrencePattern](../CircularOccurrencePattern/CircularOccurrencePattern.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ParentComponents | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the components to pattern. The valid objects that can be specified in the collection are ComponentOccurrence and OccurrencePattern objects. |
| AxisEntity | Object | Input proxy object that defines the axis of the pattern. This can be a proxy to a linear edge or work axis in a part or subassembly, or it can be a work axis from the top-level assembly. |
| AxisEntityNaturalDirection | Boolean | Input Boolean that specifies if the rotation direction of the pattern uses the natural direction of the axis entity. If True it uses the natural direction which defines the rotation direction using the right hand rule where the thumb is pointed in the direction of the axis. If False the direction is reversed. |
| AngleOffset | Variant | Input Variant that defines the angle offset between pattern instances. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |
| Count | Variant | Input Variant that defines the number of instances. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a string is input it must result in a unitless number. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |