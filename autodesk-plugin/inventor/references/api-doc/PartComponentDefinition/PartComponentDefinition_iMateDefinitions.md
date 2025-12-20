# PartComponentDefinition.iMateDefinitions Property

Parent Object: [PartComponentDefinition](../PartComponentDefinition/PartComponentDefinition.md)

## Description

Property that returns the iMateDefinitions collection object associated with this part.

## Syntax

PartComponentDefinition.**iMateDefinitions**() As [iMateDefinitions](../iMateDefinitions/iMateDefinitions.md)

## Property Value

This is a read only property whose value is an [iMateDefinitions](../iMateDefinitions/iMateDefinitions.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create rotational assembly joint](../../sample-programs/AssemblyRotationalJoint_Sample.md) | This sample demonstrates creating an assembly joint. It connects the midpoints of the edges of two faces using a rotational joint. To do this it first creates a geometry intent object of the midpoint of the edge and then creates another intent using the face and the midpoint intent. It does this to create to midpoint intents which it then uses to create the rotational connection.  The sample uses and existing part that must be set up to allow it to work correctly. To create the sample part you can use any part that has a planar face and a linear edge connected to that planar face. A simple box is sufficient. In this part Add a mate iMate to the planar face and rename the iMate to "Face1". Also add a mate iMate to a linear edge that is on the face previously named and rename this iMate to "Edge1". Save the part to "C:\Temp\SamplePart.ipt" or any other name and edit the code below to reference the file. You can then run the sample code which will create a new assembly, insert two instances of the part and create a rotational connection between them. Then it will animation the rotation by driving the connection. |
| [Add iMate Definition](../../sample-programs/iMateDefinitions_AddMateiMateDefinition_Sample.md) | Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |