# TransitionalConstraint Object

Derived from: [AssemblyConstraint](../AssemblyConstraint/AssemblyConstraint.md) Object

## Description

Object that represents a transition assembly constraint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../TransitionalConstraint/TransitionalConstraint_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../TransitionalConstraint/TransitionalConstraint_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../TransitionalConstraint/TransitionalConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TransitionalConstraint/TransitionalConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../TransitionalConstraint/TransitionalConstraint_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../TransitionalConstraint/TransitionalConstraint_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Application](../TransitionalConstraint/TransitionalConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TransitionalConstraint/TransitionalConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DriveSettings](../TransitionalConstraint/TransitionalConstraint_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../TransitionalConstraint/TransitionalConstraint_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwo](../TransitionalConstraint/TransitionalConstraint_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [GeometryOne](../TransitionalConstraint/TransitionalConstraint_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../TransitionalConstraint/TransitionalConstraint_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../TransitionalConstraint/TransitionalConstraint_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../TransitionalConstraint/TransitionalConstraint_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [IsDefaultName](../TransitionalConstraint/TransitionalConstraint_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../TransitionalConstraint/TransitionalConstraint_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../TransitionalConstraint/TransitionalConstraint_Name.md) | Gets/Sets the displayable name of this constraint. |
| [OccurrenceOne](../TransitionalConstraint/TransitionalConstraint_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../TransitionalConstraint/TransitionalConstraint_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Parent](../TransitionalConstraint/TransitionalConstraint_Parent.md) | Property that returns the parent of the object. |
| [ResultOfiMate](../TransitionalConstraint/TransitionalConstraint_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../TransitionalConstraint/TransitionalConstraint_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [Suppressed](../TransitionalConstraint/TransitionalConstraint_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [Type](../TransitionalConstraint/TransitionalConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../TransitionalConstraint/TransitionalConstraint_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Accessed From

[AngleConstraint.ConvertToTransitionalConstraint](../AngleConstraint/AngleConstraint_ConvertToTransitionalConstraint.md), [AngleConstraintProxy.ConvertToTransitionalConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToTransitionalConstraint.md), [AssemblyConstraint.ConvertToTransitionalConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToTransitionalConstraint.md), [AssemblyConstraints.AddTransitionalConstraint](../AssemblyConstraints/AssemblyConstraints_AddTransitionalConstraint.md), [AssemblySymmetryConstraint.ConvertToTransitionalConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_ConvertToTransitionalConstraint.md), [AssemblySymmetryConstraintProxy.ConvertToTransitionalConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToTransitionalConstraint.md), [CustomConstraint.ConvertToTransitionalConstraint](CustomConstraint_ConvertToTransitionalConstraint.md), [CustomConstraintProxy.ConvertToTransitionalConstraint](CustomConstraintProxy_ConvertToTransitionalConstraint.md), [FlushConstraint.ConvertToTransitionalConstraint](../FlushConstraint/FlushConstraint_ConvertToTransitionalConstraint.md), [FlushConstraintProxy.ConvertToTransitionalConstraint](../FlushConstraintProxy/FlushConstraintProxy_ConvertToTransitionalConstraint.md), [InsertConstraint.ConvertToTransitionalConstraint](../InsertConstraint/InsertConstraint_ConvertToTransitionalConstraint.md), [InsertConstraintProxy.ConvertToTransitionalConstraint](../InsertConstraintProxy/InsertConstraintProxy_ConvertToTransitionalConstraint.md), [MateConstraint.ConvertToTransitionalConstraint](../MateConstraint/MateConstraint_ConvertToTransitionalConstraint.md), [MateConstraintProxy.ConvertToTransitionalConstraint](../MateConstraintProxy/MateConstraintProxy_ConvertToTransitionalConstraint.md), [RotateRotateConstraint.ConvertToTransitionalConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToTransitionalConstraint.md), [RotateRotateConstraintProxy.ConvertToTransitionalConstraint](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_ConvertToTransitionalConstraint.md), [RotateTranslateConstraint.ConvertToTransitionalConstraint](../RotateTranslateConstraint/RotateTranslateConstraint_ConvertToTransitionalConstraint.md), [RotateTranslateConstraintProxy.ConvertToTransitionalConstraint](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_ConvertToTransitionalConstraint.md), [TangentConstraint.ConvertToTransitionalConstraint](../TangentConstraint/TangentConstraint_ConvertToTransitionalConstraint.md), [TangentConstraintProxy.ConvertToTransitionalConstraint](../TangentConstraintProxy/TangentConstraintProxy_ConvertToTransitionalConstraint.md), [TransitionalConstraint.ConvertToTransitionalConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToTransitionalConstraint.md), [TransitionalConstraintProxy.ConvertToTransitionalConstraint](../TransitionalConstraintProxy/TransitionalConstraintProxy_ConvertToTransitionalConstraint.md), [TransitionalConstraintProxy.NativeObject](../TransitionalConstraintProxy/TransitionalConstraintProxy_NativeObject.md), [TranslateTranslateConstraint.ConvertToTransitionalConstraint](../TranslateTranslateConstraint/TranslateTranslateConstraint_ConvertToTransitionalConstraint.md), [TranslateTranslateConstraintProxy.ConvertToTransitionalConstraint](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_ConvertToTransitionalConstraint.md)

## Derived Classes

[TransitionalConstraintProxy](../TransitionalConstraintProxy/TransitionalConstraintProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |