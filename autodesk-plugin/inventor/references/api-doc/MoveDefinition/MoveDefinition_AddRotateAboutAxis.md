# MoveDefinition.AddRotateAboutAxis Method

Parent Object: [MoveDefinition](../MoveDefinition/MoveDefinition.md)

## Description

Method that creates a move rotate about azis operation on the associated move body feature.

## Syntax

MoveDefinition.**AddRotateAboutAxis**( ***AxisEntity*** As Object, ***UseNaturalAxisDirection*** As Boolean, ***Angle*** As Variant ) As [RotateAboutLineMoveOperation](../RotateAboutLineMoveOperation/RotateAboutLineMoveOperation.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AxisEntity | Object | Input entity that defines the axis of rotation Valid input includes linear edges, cylindrical faces, torus faces, and work axes. The rotation of the body(s) about this entity is defined using the right-hand rule, where the thumb is pointed along the entity in its natural direction and the fingers define the direction of rotation. The UseEntityNaturalDirection property can be used to reverse the rotation direction. |
| UseNaturalAxisDirection | Boolean | Input Boolean that specifies if the rotation direction of the bodies uses the natural direction of the direction entity. If True it uses the natural direction. If False the direction is reversed. The rotation of the body(s) about the axis entity is defined using the right-hand rule, where the thumb is pointed along the entity in its natural direction and the fingers define the direction of rotation. The UseEntityNaturalDirection property can be used to reverse the rotation direction. |
| Angle | Variant | Input Variant that defines the rotation angle of the rotate operation. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move Feature Creation](../../sample-programs/MoveBodyFeatures_Sample.md) | Demonstrates the creation of a Move feature. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |