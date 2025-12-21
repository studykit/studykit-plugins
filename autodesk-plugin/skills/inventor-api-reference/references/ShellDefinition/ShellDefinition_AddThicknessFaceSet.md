# ShellDefinition.AddThicknessFaceSet Method

Parent Object: [ShellDefinition](../ShellDefinition/ShellDefinition.md)

## Description

Method that creates a new thickness face set. The new ShellThicknessFaceSet is returned.

## Syntax

ShellDefinition.**AddThicknessFaceSet**( ***Faces*** As [FaceCollection](../FaceCollection/FaceCollection.md), ***Thickness*** As Variant ) As [ShellThicknessFaceSet](../ShellThicknessFaceSet/ShellThicknessFaceSet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Faces | [FaceCollection](../FaceCollection/FaceCollection.md) | Input FaceCollection object that contains faces that have a unique thickness defined. |
| Thickness | Variant | Input Variant that defines the unique thickness associated with the input Faces. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document. |

## Version

Introduced in version 9
