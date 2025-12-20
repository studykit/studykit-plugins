# AssemblyJointDefinition Object

## Description

The AssemblyJointDefinition is not an assembly joint but is an object that contains all of the information that defines an assembly joint. It is used to create new joints and to edit existing joints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../AssemblyJointDefinition/AssemblyJointDefinition_Copy.md) | Method that creates a copy of this AssemblyJointDefinition object. The new AssemblyJointDefinition is independent of any assembly joint. It can be edited and used as input to edit an existing joint or to create a new assembly joint. |
| [SetOriginOneAsBetweenTwoFaces](../AssemblyJointDefinition/AssemblyJointDefinition_SetOriginOneAsBetweenTwoFaces.md) | Method that sets assembly joint origin as between two faces origin for OriginOne. |
| [SetOriginOneAsInfer](../AssemblyJointDefinition/AssemblyJointDefinition_SetOriginOneAsInfer.md) | Method that sets assembly joint origin as infer origin for OriginOne. |
| [SetOriginOneAsOffset](../AssemblyJointDefinition/AssemblyJointDefinition_SetOriginOneAsOffset.md) | Method that sets assembly joint origin as offset origin for OriginOne. |
| [SetOriginTwoAsBetweenTwoFaces](../AssemblyJointDefinition/AssemblyJointDefinition_SetOriginTwoAsBetweenTwoFaces.md) | Method that sets assembly joint origin as between two faces origin for OriginTwo. |
| [SetOriginTwoAsInfer](../AssemblyJointDefinition/AssemblyJointDefinition_SetOriginTwoAsInfer.md) | Method that sets assembly joint origin as infer origin for OriginTwo. |
| [SetOriginTwoAsOffset](../AssemblyJointDefinition/AssemblyJointDefinition_SetOriginTwoAsOffset.md) | Method that sets assembly joint origin as offset origin for OriginTwo. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AlignmentOne](../AssemblyJointDefinition/AssemblyJointDefinition_AlignmentOne.md) | Read-write property that gets and sets the geometry object that defines the first alignment for the assembly joint. |
| [AlignmentTwo](../AssemblyJointDefinition/AssemblyJointDefinition_AlignmentTwo.md) | Read-write property that gets and sets the geometry object that defines the alignment for the second component. |
| [AngularPosition](../AssemblyJointDefinition/AssemblyJointDefinition_AngularPosition.md) | Read-write property that gets and sets the angular position around the origin direction of the first occurrence the assembly joint object is between with. |
| [AngularPositionEndLimit](../AssemblyJointDefinition/AssemblyJointDefinition_AngularPositionEndLimit.md) | Read-write property that gets and sets the angular position end limit for the assembly joint object. |
| [AngularPositionStartLimit](../AssemblyJointDefinition/AssemblyJointDefinition_AngularPositionStartLimit.md) | Read-write property that gets and sets the angular position start limit for the assembly joint object. |
| [Application](../AssemblyJointDefinition/AssemblyJointDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [FlipAlignmentDirection](../AssemblyJointDefinition/AssemblyJointDefinition_FlipAlignmentDirection.md) | Read-write property that gets and sets whether flip the alignment direction defined by AlignmentOne. |
| [FlipOriginDirection](../AssemblyJointDefinition/AssemblyJointDefinition_FlipOriginDirection.md) | Read-write property that gets and sets whether flip the origin direction defined by OriginOne. |
| [Gap](../AssemblyJointDefinition/AssemblyJointDefinition_Gap.md) | Read-write property that gets and sets the translation between the first and second origins along the Z-axis. |
| [HasAngularPositionLimits](../AssemblyJointDefinition/AssemblyJointDefinition_HasAngularPositionLimits.md) | Read-write property that indicates if the assembly joint has angular position start and end limits that the angular position value should not exceed to be valid. |
| [HasLinearPositionEndLimit](../AssemblyJointDefinition/AssemblyJointDefinition_HasLinearPositionEndLimit.md) | Read-write property that indicates if the assembly joint has linear position end limit that the linear position value should not exceed to be valid. |
| [HasLinearPositionStartLimit](../AssemblyJointDefinition/AssemblyJointDefinition_HasLinearPositionStartLimit.md) | Read-write property that indicates if the assembly joint has linear position start limit that the linear position value should not be less than it to be valid. |
| [JointType](../AssemblyJointDefinition/AssemblyJointDefinition_JointType.md) | Read-write property that gets and sets the type of AssemblyJoint. |
| [LinearPosition](../AssemblyJointDefinition/AssemblyJointDefinition_LinearPosition.md) | Read-write property that gets and sets the linear position of the first occurrence relative to the second occurrence that the assembly joint object. |
| [LinearPositionEndLimit](../AssemblyJointDefinition/AssemblyJointDefinition_LinearPositionEndLimit.md) | Read-write property that gets and sets the linear position end limit for the assembly joint object. |
| [LinearPositionStartLimit](../AssemblyJointDefinition/AssemblyJointDefinition_LinearPositionStartLimit.md) | Read-write property that gets and sets the linear position start limit for the assembly joint object. |
| [OriginOne](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOne.md) | Read-write property that gets and sets the first origin associated with the assembly joint object. |
| [OriginOneDefinitionType](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOneDefinitionType.md) | Read-only property that returns the definition type of the first joint origin. |
| [OriginOneReferencedFaces](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOneReferencedFaces.md) | Read-only property that returns the two referenced planar faces to define the projecting plane for OriginOne. This returns Nothing if the OriginOneDefinitonType is not equal to kBetweenTwoFacesOriginDefinitionType. |
| [OriginOneXOffset](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOneXOffset.md) | Read-only property that returns the offset of the OriginOne along origin X-axis direction. This returns Empty if the OriginOneDefinitonType is not equal to kOffsetOriginDefinitionType. |
| [OriginOneXOffsetReferencedGeometry](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOneXOffsetReferencedGeometry.md) | Read-only property that returns the referenced geometry that used to define the offset of the OriginOne along X-axis direction. This returns Nothing if the offset is not referencing any geometry. |
| [OriginOneYOffset](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOneYOffset.md) | Read-only property that returns the offset of the OriginOne along origin Y-axis direction. This returns Empty if the OriginOneDefinitonType is not equal to kOffsetOriginDefinitionType. |
| [OriginOneYOffsetReferencedGeometry](../AssemblyJointDefinition/AssemblyJointDefinition_OriginOneYOffsetReferencedGeometry.md) | Read-only property that returns the referenced geometry that used to define the offset of the OriginOne along Y-axis direction. This returns Nothing if the offset is not referencing any geometry. |
| [OriginTwo](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwo.md) | Read-write property that gets and sets the second origin associated with the assembly joint object. |
| [OriginTwoDefinitionType](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwoDefinitionType.md) | Read-only property that returns the definition type of the second joint origin. |
| [OriginTwoReferencedFaces](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwoReferencedFaces.md) | Read-only property that returns the two referenced planar faces to define the projecting plane for OriginTwo. This returns Nothing if the OriginTwoDefinitonType is not equal to kBetweenTwoFacesOriginDefinitionType. |
| [OriginTwoXOffset](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwoXOffset.md) | Read-only property that returns the offset of the OriginTwo along origin X-axis direction. This returns Empty if the OriginTwoDefinitonType is not equal to kOffsetOriginDefinitionType. |
| [OriginTwoXOffsetReferencedGeometry](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwoXOffsetReferencedGeometry.md) | Read-only property that returns the referenced geometry that used to define the offset of the OriginTwo along X-axis direction. This returns Nothing if the offset is not referencing any geometry. |
| [OriginTwoYOffset](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwoYOffset.md) | Read-only property that returns the offset of the OriginTwo along origin Y-axis direction. This returns Empty if the OriginTwoDefinitonType is not equal to kOffsetOriginDefinitionType. |
| [OriginTwoYOffsetReferencedGeometry](../AssemblyJointDefinition/AssemblyJointDefinition_OriginTwoYOffsetReferencedGeometry.md) | Read-only property that returns the referenced geometry that used to define the offset of the OriginTwo along Y-axis direction. This returns Nothing if the offset is not referencing any geometry. |
| [Parent](../AssemblyJointDefinition/AssemblyJointDefinition_Parent.md) | Read-only property that returns the parent AssemblyJoint object. This returns Nothing when the AssemblyJointDefinition is not associated with an AssemblyJoint object. |
| [Type](../AssemblyJointDefinition/AssemblyJointDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyJoint.Definition](../AssemblyJoint/AssemblyJoint_Definition.md), [AssemblyJointDefinition.Copy](../AssemblyJointDefinition/AssemblyJointDefinition_Copy.md), [AssemblyJointProxy.Definition](../AssemblyJointProxy/AssemblyJointProxy_Definition.md), [AssemblyJoints.CreateAssemblyJointDefinition](../AssemblyJoints/AssemblyJoints_CreateAssemblyJointDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create planar AssemblyJoint with offset to origins](../../sample-programs/AssemblyJointDefinition_SetOriginOneAsOffset_Sample.md) | This sample demonstrates how to create a planar AssemblyJoint with offset to the OriginOne and OriginTwo. |
| [Create rotational assembly joint](../../sample-programs/AssemblyRotationalJoint_Sample.md) | This sample demonstrates creating an assembly joint. It connects the midpoints of the edges of two faces using a rotational joint. To do this it first creates a geometry intent object of the midpoint of the edge and then creates another intent using the face and the midpoint intent. It does this to create to midpoint intents which it then uses to create the rotational connection.  The sample uses and existing part that must be set up to allow it to work correctly. To create the sample part you can use any part that has a planar face and a linear edge connected to that planar face. A simple box is sufficient. In this part Add a mate iMate to the planar face and rename the iMate to "Face1". Also add a mate iMate to a linear edge that is on the face previously named and rename this iMate to "Edge1". Save the part to "C:\Temp\SamplePart.ipt" or any other name and edit the code below to reference the file. You can then run the sample code which will create a new assembly, insert two instances of the part and create a rotational connection between them. Then it will animation the rotation by driving the connection. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |