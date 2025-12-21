# AssemblyJointProxy Object

Derived from: [AssemblyJoint](../AssemblyJoint/AssemblyJoint.md) Object

## Description

Represents an AssemblyJoint object in a subaussembly within another assemby.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../AssemblyJointProxy/AssemblyJointProxy_Delete.md) | Method that deletes the AssemblyJoint object. |
| [GetReferenceKey](../AssemblyJointProxy/AssemblyJointProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../AssemblyJointProxy/AssemblyJointProxy_AffectedOccurrenceOne.md) | Read-only property that returns the first of the two occurrences affected by this joint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this joint is between. |
| [AffectedOccurrenceTwo](../AssemblyJointProxy/AssemblyJointProxy_AffectedOccurrenceTwo.md) | Read-only property that returns the second of the two occurrences affected by this joint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this joint is between. |
| [Application](../AssemblyJointProxy/AssemblyJointProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AssemblyJointProxy/AssemblyJointProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../AssemblyJointProxy/AssemblyJointProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../AssemblyJointProxy/AssemblyJointProxy_Definition.md) | Read-write property that gets and sets the AssemblyJointDefinition object associated with this assembly joint object. |
| [DriveSettings](../AssemblyJointProxy/AssemblyJointProxy_DriveSettings.md) | Read-only property that returns the DriveSettings object associated with this joint. |
| [HealthStatus](../AssemblyJointProxy/AssemblyJointProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [Locked](../AssemblyJointProxy/AssemblyJointProxy_Locked.md) | Read-write property that gets and sets whether the degree of freedom of the assembly joint is locked or not. |
| [Name](../AssemblyJointProxy/AssemblyJointProxy_Name.md) | Read-write property that gets and sets the name of the assembly joint. |
| [NativeObject](../AssemblyJointProxy/AssemblyJointProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OccurrenceOne](../AssemblyJointProxy/AssemblyJointProxy_OccurrenceOne.md) | Read-only property that returns the first of the two components this assembly joint is between. |
| [OccurrenceTwo](../AssemblyJointProxy/AssemblyJointProxy_OccurrenceTwo.md) | Read-only property that returns the second of the two components this assembly joint is between. |
| [Parent](../AssemblyJointProxy/AssemblyJointProxy_Parent.md) | Read-only property that returns the parent AssemblyComponentDefinition object. |
| [Protected](../AssemblyJointProxy/AssemblyJointProxy_Protected.md) | Read-write property that gets and sets whether the degree of freedom of the assembly joint is protected or not. |
| [Suppressed](../AssemblyJointProxy/AssemblyJointProxy_Suppressed.md) | Read-write property that gets and sets whether the assembly joint is suppressed or not. |
| [Type](../AssemblyJointProxy/AssemblyJointProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AssemblyJointProxy/AssemblyJointProxy_Visible.md) | Read-write property that gets and sets the visibility of the object. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |