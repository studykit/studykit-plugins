# AssemblyJoints Object

## Description

The AssemblyJoints object is a collection that provides access to all of the existing assembly joints in the document and provided access to the functions to create new joints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../AssemblyJoints/AssemblyJoints_Add.md) | Method that creates a new AssemblyJoint. The new created AssemblyJoint is returned. |
| [CreateAssemblyJointDefinition](../AssemblyJoints/AssemblyJoints_CreateAssemblyJointDefinition.md) | Method that creates a new AssemblyJointDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AssemblyJoints/AssemblyJoints_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../AssemblyJoints/AssemblyJoints_Count.md) | Property that returns the number of items in this collection. |
| [Item](../AssemblyJoints/AssemblyJoints_Item.md) | Read-only property that returns the specified AssemblyJoint object from the collection. |
| [Type](../AssemblyJoints/AssemblyJoints_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.Joints](../AssemblyComponentDefinition/AssemblyComponentDefinition_Joints.md), [WeldmentComponentDefinition.Joints](../WeldmentComponentDefinition/WeldmentComponentDefinition_Joints.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create rotational assembly joint](../../sample-programs/AssemblyRotationalJoint_Sample.md) | This sample demonstrates creating an assembly joint. It connects the midpoints of the edges of two faces using a rotational joint. To do this it first creates a geometry intent object of the midpoint of the edge and then creates another intent using the face and the midpoint intent. It does this to create to midpoint intents which it then uses to create the rotational connection.  The sample uses and existing part that must be set up to allow it to work correctly. To create the sample part you can use any part that has a planar face and a linear edge connected to that planar face. A simple box is sufficient. In this part Add a mate iMate to the planar face and rename the iMate to "Face1". Also add a mate iMate to a linear edge that is on the face previously named and rename this iMate to "Edge1". Save the part to "C:\Temp\SamplePart.ipt" or any other name and edit the code below to reference the file. You can then run the sample code which will create a new assembly, insert two instances of the part and create a rotational connection between them. Then it will animation the rotation by driving the connection. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |