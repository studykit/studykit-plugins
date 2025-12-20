# RotateRotateConstraint Object

Derived from: [AssemblyConstraint](../AssemblyConstraint/AssemblyConstraint.md) Object

## Description

Object that represents a rotation motion constraint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../RotateRotateConstraint/RotateRotateConstraint_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../RotateRotateConstraint/RotateRotateConstraint_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../RotateRotateConstraint/RotateRotateConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../RotateRotateConstraint/RotateRotateConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../RotateRotateConstraint/RotateRotateConstraint_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../RotateRotateConstraint/RotateRotateConstraint_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Application](../RotateRotateConstraint/RotateRotateConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RotateRotateConstraint/RotateRotateConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DriveSettings](../RotateRotateConstraint/RotateRotateConstraint_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../RotateRotateConstraint/RotateRotateConstraint_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwo](../RotateRotateConstraint/RotateRotateConstraint_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [ForwardDirection](../RotateRotateConstraint/RotateRotateConstraint_ForwardDirection.md) | Boolean property that returns the direction of rotation of the objects with respect to the axis direction. If True, both objects will rotate in the same direction around their axes. If False, then they will rotate in opposite directions. |
| [GeometryOne](../RotateRotateConstraint/RotateRotateConstraint_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../RotateRotateConstraint/RotateRotateConstraint_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../RotateRotateConstraint/RotateRotateConstraint_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../RotateRotateConstraint/RotateRotateConstraint_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [IsDefaultName](../RotateRotateConstraint/RotateRotateConstraint_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../RotateRotateConstraint/RotateRotateConstraint_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../RotateRotateConstraint/RotateRotateConstraint_Name.md) | Gets/Sets the displayable name of this constraint. |
| [OccurrenceOne](../RotateRotateConstraint/RotateRotateConstraint_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../RotateRotateConstraint/RotateRotateConstraint_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Parent](../RotateRotateConstraint/RotateRotateConstraint_Parent.md) | Property that returns the parent of the object. |
| [Ratio](../RotateRotateConstraint/RotateRotateConstraint_Ratio.md) | Property that returns the Parameter object that controls the rotation ratio of the constraint. |
| [ResultOfiMate](../RotateRotateConstraint/RotateRotateConstraint_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../RotateRotateConstraint/RotateRotateConstraint_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [Suppressed](../RotateRotateConstraint/RotateRotateConstraint_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [Type](../RotateRotateConstraint/RotateRotateConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../RotateRotateConstraint/RotateRotateConstraint_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Accessed From

[AngleConstraint.ConvertToRotateRotateConstraint](../AngleConstraint/AngleConstraint_ConvertToRotateRotateConstraint.md), [AngleConstraintProxy.ConvertToRotateRotateConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToRotateRotateConstraint.md), [AssemblyConstraint.ConvertToRotateRotateConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToRotateRotateConstraint.md), [AssemblyConstraints.AddRotateRotateConstraint](../AssemblyConstraints/AssemblyConstraints_AddRotateRotateConstraint.md), [AssemblySymmetryConstraint.ConvertToRotateRotateConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_ConvertToRotateRotateConstraint.md), [AssemblySymmetryConstraintProxy.ConvertToRotateRotateConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToRotateRotateConstraint.md), [CustomConstraint.ConvertToRotateRotateConstraint](CustomConstraint_ConvertToRotateRotateConstraint.md), [CustomConstraintProxy.ConvertToRotateRotateConstraint](CustomConstraintProxy_ConvertToRotateRotateConstraint.md), [FlushConstraint.ConvertToRotateRotateConstraint](../FlushConstraint/FlushConstraint_ConvertToRotateRotateConstraint.md), [FlushConstraintProxy.ConvertToRotateRotateConstraint](../FlushConstraintProxy/FlushConstraintProxy_ConvertToRotateRotateConstraint.md), [InsertConstraint.ConvertToRotateRotateConstraint](../InsertConstraint/InsertConstraint_ConvertToRotateRotateConstraint.md), [InsertConstraintProxy.ConvertToRotateRotateConstraint](../InsertConstraintProxy/InsertConstraintProxy_ConvertToRotateRotateConstraint.md), [MateConstraint.ConvertToRotateRotateConstraint](../MateConstraint/MateConstraint_ConvertToRotateRotateConstraint.md), [MateConstraintProxy.ConvertToRotateRotateConstraint](../MateConstraintProxy/MateConstraintProxy_ConvertToRotateRotateConstraint.md), [RotateRotateConstraint.ConvertToRotateRotateConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToRotateRotateConstraint.md), [RotateRotateConstraintProxy.ConvertToRotateRotateConstraint](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_ConvertToRotateRotateConstraint.md), [RotateRotateConstraintProxy.NativeObject](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_NativeObject.md), [RotateTranslateConstraint.ConvertToRotateRotateConstraint](../RotateTranslateConstraint/RotateTranslateConstraint_ConvertToRotateRotateConstraint.md), [RotateTranslateConstraintProxy.ConvertToRotateRotateConstraint](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_ConvertToRotateRotateConstraint.md), [TangentConstraint.ConvertToRotateRotateConstraint](../TangentConstraint/TangentConstraint_ConvertToRotateRotateConstraint.md), [TangentConstraintProxy.ConvertToRotateRotateConstraint](../TangentConstraintProxy/TangentConstraintProxy_ConvertToRotateRotateConstraint.md), [TransitionalConstraint.ConvertToRotateRotateConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToRotateRotateConstraint.md), [TransitionalConstraintProxy.ConvertToRotateRotateConstraint](../TransitionalConstraintProxy/TransitionalConstraintProxy_ConvertToRotateRotateConstraint.md), [TranslateTranslateConstraint.ConvertToRotateRotateConstraint](../TranslateTranslateConstraint/TranslateTranslateConstraint_ConvertToRotateRotateConstraint.md), [TranslateTranslateConstraintProxy.ConvertToRotateRotateConstraint](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_ConvertToRotateRotateConstraint.md)

## Derived Classes

[RotateRotateConstraintProxy](../RotateRotateConstraintProxy/RotateRotateConstraintProxy.md)

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |