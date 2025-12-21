# AssemblyJoint Object

## Description

An AssemblyJoint object represents an assembly relationship between two components that defines those components connect.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../AssemblyJoint/AssemblyJoint_Delete.md) | Method that deletes the AssemblyJoint object. |
| [GetReferenceKey](../AssemblyJoint/AssemblyJoint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../AssemblyJoint/AssemblyJoint_AffectedOccurrenceOne.md) | Read-only property that returns the first of the two occurrences affected by this joint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this joint is between. |
| [AffectedOccurrenceTwo](../AssemblyJoint/AssemblyJoint_AffectedOccurrenceTwo.md) | Read-only property that returns the second of the two occurrences affected by this joint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this joint is between. |
| [Application](../AssemblyJoint/AssemblyJoint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AssemblyJoint/AssemblyJoint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Definition](../AssemblyJoint/AssemblyJoint_Definition.md) | Read-write property that gets and sets the AssemblyJointDefinition object associated with this assembly joint object. |
| [DriveSettings](../AssemblyJoint/AssemblyJoint_DriveSettings.md) | Read-only property that returns the DriveSettings object associated with this joint. |
| [HealthStatus](../AssemblyJoint/AssemblyJoint_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [Locked](../AssemblyJoint/AssemblyJoint_Locked.md) | Read-write property that gets and sets whether the degree of freedom of the assembly joint is locked or not. |
| [Name](../AssemblyJoint/AssemblyJoint_Name.md) | Read-write property that gets and sets the name of the assembly joint. |
| [OccurrenceOne](../AssemblyJoint/AssemblyJoint_OccurrenceOne.md) | Read-only property that returns the first of the two components this assembly joint is between. |
| [OccurrenceTwo](../AssemblyJoint/AssemblyJoint_OccurrenceTwo.md) | Read-only property that returns the second of the two components this assembly joint is between. |
| [Parent](../AssemblyJoint/AssemblyJoint_Parent.md) | Read-only property that returns the parent AssemblyComponentDefinition object. |
| [Protected](../AssemblyJoint/AssemblyJoint_Protected.md) | Read-write property that gets and sets whether the degree of freedom of the assembly joint is protected or not. |
| [Suppressed](../AssemblyJoint/AssemblyJoint_Suppressed.md) | Read-write property that gets and sets whether the assembly joint is suppressed or not. |
| [Type](../AssemblyJoint/AssemblyJoint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AssemblyJoint/AssemblyJoint_Visible.md) | Read-write property that gets and sets the visibility of the object. |

## Accessed From

[AssemblyJointDefinition.Parent](../AssemblyJointDefinition/AssemblyJointDefinition_Parent.md), [AssemblyJointProxy.NativeObject](../AssemblyJointProxy/AssemblyJointProxy_NativeObject.md), [AssemblyJoints.Add](../AssemblyJoints/AssemblyJoints_Add.md), [AssemblyJoints.Item](../AssemblyJoints/AssemblyJoints_Item.md), [AssemblyJointsEnumerator.Item](../AssemblyJointsEnumerator/AssemblyJointsEnumerator_Item.md)

## Derived Classes

[AssemblyJointProxy](../AssemblyJointProxy/AssemblyJointProxy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create planar AssemblyJoint with offset to origins](../../sample-programs/AssemblyJointDefinition_SetOriginOneAsOffset_Sample.md) | This sample demonstrates how to create a planar AssemblyJoint with offset to the OriginOne and OriginTwo. |

## Version

Introduced in version 2014
