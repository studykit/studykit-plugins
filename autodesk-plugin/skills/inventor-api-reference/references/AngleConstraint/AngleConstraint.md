# AngleConstraint Object

Derived from: [AssemblyConstraint](../AssemblyConstraint/AssemblyConstraint.md) Object

## Description

Object that represents an angle assembly constraint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../AngleConstraint/AngleConstraint_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../AngleConstraint/AngleConstraint_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../AngleConstraint/AngleConstraint_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../AngleConstraint/AngleConstraint_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../AngleConstraint/AngleConstraint_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../AngleConstraint/AngleConstraint_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../AngleConstraint/AngleConstraint_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../AngleConstraint/AngleConstraint_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../AngleConstraint/AngleConstraint_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../AngleConstraint/AngleConstraint_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../AngleConstraint/AngleConstraint_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../AngleConstraint/AngleConstraint_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../AngleConstraint/AngleConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../AngleConstraint/AngleConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../AngleConstraint/AngleConstraint_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../AngleConstraint/AngleConstraint_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Angle](../AngleConstraint/AngleConstraint_Angle.md) | Property that returns the object that controls the angle of the constraint. |
| [Application](../AngleConstraint/AngleConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AngleConstraint/AngleConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConstraintLimits](../AngleConstraint/AngleConstraint_ConstraintLimits.md) | Property that returns the ConstraintLimits object that provides access to various limits related settings for the constraint. |
| [DriveSettings](../AngleConstraint/AngleConstraint_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../AngleConstraint/AngleConstraint_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwo](../AngleConstraint/AngleConstraint_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [GeometryOne](../AngleConstraint/AngleConstraint_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../AngleConstraint/AngleConstraint_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../AngleConstraint/AngleConstraint_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../AngleConstraint/AngleConstraint_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [IsDefaultName](../AngleConstraint/AngleConstraint_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../AngleConstraint/AngleConstraint_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../AngleConstraint/AngleConstraint_Name.md) | Gets/Sets the displayable name of this constraint. |
| [OccurrenceOne](../AngleConstraint/AngleConstraint_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../AngleConstraint/AngleConstraint_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Parent](../AngleConstraint/AngleConstraint_Parent.md) | Property that returns the parent of the object. |
| [ReferenceVectorEntity](../AngleConstraint/AngleConstraint_ReferenceVectorEntity.md) | Property that returns the third (reference vector) entity the constraint it tied to. |
| [ResultOfiMate](../AngleConstraint/AngleConstraint_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../AngleConstraint/AngleConstraint_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [SolutionType](../AngleConstraint/AngleConstraint_SolutionType.md) | Property that returns the solution type. |
| [Suppressed](../AngleConstraint/AngleConstraint_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [Type](../AngleConstraint/AngleConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AngleConstraint/AngleConstraint_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Accessed From

[AngleConstraint.ConvertToAngleConstraint](../AngleConstraint/AngleConstraint_ConvertToAngleConstraint.md), [AngleConstraintProxy.ConvertToAngleConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToAngleConstraint.md), [AngleConstraintProxy.NativeObject](../AngleConstraintProxy/AngleConstraintProxy_NativeObject.md), [AssemblyConstraint.ConvertToAngleConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToAngleConstraint.md), [AssemblyConstraints.AddAngleConstraint](../AssemblyConstraints/AssemblyConstraints_AddAngleConstraint.md), [AssemblySymmetryConstraint.ConvertToAngleConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_ConvertToAngleConstraint.md), [AssemblySymmetryConstraintProxy.ConvertToAngleConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToAngleConstraint.md), [CustomConstraint.ConvertToAngleConstraint](CustomConstraint_ConvertToAngleConstraint.md), [CustomConstraintProxy.ConvertToAngleConstraint](CustomConstraintProxy_ConvertToAngleConstraint.md), [FlushConstraint.ConvertToAngleConstraint](../FlushConstraint/FlushConstraint_ConvertToAngleConstraint.md), [FlushConstraintProxy.ConvertToAngleConstraint](../FlushConstraintProxy/FlushConstraintProxy_ConvertToAngleConstraint.md), [InsertConstraint.ConvertToAngleConstraint](../InsertConstraint/InsertConstraint_ConvertToAngleConstraint.md), [InsertConstraintProxy.ConvertToAngleConstraint](../InsertConstraintProxy/InsertConstraintProxy_ConvertToAngleConstraint.md), [LayoutConstraint.ZAngleConstraint](../LayoutConstraint/LayoutConstraint_ZAngleConstraint.md), [LayoutConstraintProxy.ZAngleConstraint](../LayoutConstraintProxy/LayoutConstraintProxy_ZAngleConstraint.md), [MateConstraint.ConvertToAngleConstraint](../MateConstraint/MateConstraint_ConvertToAngleConstraint.md), [MateConstraintProxy.ConvertToAngleConstraint](../MateConstraintProxy/MateConstraintProxy_ConvertToAngleConstraint.md), [RotateRotateConstraint.ConvertToAngleConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToAngleConstraint.md), [RotateRotateConstraintProxy.ConvertToAngleConstraint](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_ConvertToAngleConstraint.md), [RotateTranslateConstraint.ConvertToAngleConstraint](../RotateTranslateConstraint/RotateTranslateConstraint_ConvertToAngleConstraint.md), [RotateTranslateConstraintProxy.ConvertToAngleConstraint](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_ConvertToAngleConstraint.md), [TangentConstraint.ConvertToAngleConstraint](../TangentConstraint/TangentConstraint_ConvertToAngleConstraint.md), [TangentConstraintProxy.ConvertToAngleConstraint](../TangentConstraintProxy/TangentConstraintProxy_ConvertToAngleConstraint.md), [TransitionalConstraint.ConvertToAngleConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToAngleConstraint.md), [TransitionalConstraintProxy.ConvertToAngleConstraint](../TransitionalConstraintProxy/TransitionalConstraintProxy_ConvertToAngleConstraint.md), [TranslateTranslateConstraint.ConvertToAngleConstraint](../TranslateTranslateConstraint/TranslateTranslateConstraint_ConvertToAngleConstraint.md), [TranslateTranslateConstraintProxy.ConvertToAngleConstraint](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_ConvertToAngleConstraint.md)

## Derived Classes

[AngleConstraintProxy](../AngleConstraintProxy/AngleConstraintProxy.md)

## Version

Introduced in version 4
