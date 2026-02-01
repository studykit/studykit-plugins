# TangentConstraint Object

Derived from: [AssemblyConstraint](../AssemblyConstraint/AssemblyConstraint.md) Object

## Description

Object that represents a tangent assembly constraint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../TangentConstraint/TangentConstraint_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../TangentConstraint/TangentConstraint_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../TangentConstraint/TangentConstraint_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../TangentConstraint/TangentConstraint_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../TangentConstraint/TangentConstraint_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../TangentConstraint/TangentConstraint_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../TangentConstraint/TangentConstraint_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../TangentConstraint/TangentConstraint_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../TangentConstraint/TangentConstraint_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../TangentConstraint/TangentConstraint_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../TangentConstraint/TangentConstraint_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../TangentConstraint/TangentConstraint_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../TangentConstraint/TangentConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../TangentConstraint/TangentConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../TangentConstraint/TangentConstraint_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../TangentConstraint/TangentConstraint_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Application](../TangentConstraint/TangentConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../TangentConstraint/TangentConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConstraintLimits](../TangentConstraint/TangentConstraint_ConstraintLimits.md) | Property that returns the ConstraintLimits object that provides access to various limits related settings for the constraint. |
| [DriveSettings](../TangentConstraint/TangentConstraint_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../TangentConstraint/TangentConstraint_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwo](../TangentConstraint/TangentConstraint_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [GeometryOne](../TangentConstraint/TangentConstraint_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../TangentConstraint/TangentConstraint_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../TangentConstraint/TangentConstraint_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../TangentConstraint/TangentConstraint_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [InsideTangency](../TangentConstraint/TangentConstraint_InsideTangency.md) | Property that returns whether the curvatures of the surfaces at the point of tangency are on the same side. True if they are on the same side. |
| [IsDefaultName](../TangentConstraint/TangentConstraint_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../TangentConstraint/TangentConstraint_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../TangentConstraint/TangentConstraint_Name.md) | Gets/Sets the displayable name of this constraint. |
| [OccurrenceOne](../TangentConstraint/TangentConstraint_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../TangentConstraint/TangentConstraint_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Offset](../TangentConstraint/TangentConstraint_Offset.md) | Property that returns the Parameter object that controls the offset distance of the constraint. |
| [Parent](../TangentConstraint/TangentConstraint_Parent.md) | Property that returns the parent of the object. |
| [ResultOfiMate](../TangentConstraint/TangentConstraint_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../TangentConstraint/TangentConstraint_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [Suppressed](../TangentConstraint/TangentConstraint_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [Type](../TangentConstraint/TangentConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../TangentConstraint/TangentConstraint_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Accessed From

[AngleConstraint.ConvertToTangentConstraint](../AngleConstraint/AngleConstraint_ConvertToTangentConstraint.md), [AngleConstraintProxy.ConvertToTangentConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToTangentConstraint.md), [AssemblyConstraint.ConvertToTangentConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToTangentConstraint.md), [AssemblyConstraints.AddTangentConstraint](../AssemblyConstraints/AssemblyConstraints_AddTangentConstraint.md), [AssemblySymmetryConstraint.ConvertToTangentConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_ConvertToTangentConstraint.md), [AssemblySymmetryConstraintProxy.ConvertToTangentConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToTangentConstraint.md), [CustomConstraint.ConvertToTangentConstraint](CustomConstraint_ConvertToTangentConstraint.md), [CustomConstraintProxy.ConvertToTangentConstraint](CustomConstraintProxy_ConvertToTangentConstraint.md), [FlushConstraint.ConvertToTangentConstraint](../FlushConstraint/FlushConstraint_ConvertToTangentConstraint.md), [FlushConstraintProxy.ConvertToTangentConstraint](../FlushConstraintProxy/FlushConstraintProxy_ConvertToTangentConstraint.md), [InsertConstraint.ConvertToTangentConstraint](../InsertConstraint/InsertConstraint_ConvertToTangentConstraint.md), [InsertConstraintProxy.ConvertToTangentConstraint](../InsertConstraintProxy/InsertConstraintProxy_ConvertToTangentConstraint.md), [MateConstraint.ConvertToTangentConstraint](../MateConstraint/MateConstraint_ConvertToTangentConstraint.md), [MateConstraintProxy.ConvertToTangentConstraint](../MateConstraintProxy/MateConstraintProxy_ConvertToTangentConstraint.md), [RotateRotateConstraint.ConvertToTangentConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToTangentConstraint.md), [RotateRotateConstraintProxy.ConvertToTangentConstraint](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_ConvertToTangentConstraint.md), [RotateTranslateConstraint.ConvertToTangentConstraint](../RotateTranslateConstraint/RotateTranslateConstraint_ConvertToTangentConstraint.md), [RotateTranslateConstraintProxy.ConvertToTangentConstraint](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_ConvertToTangentConstraint.md), [TangentConstraint.ConvertToTangentConstraint](../TangentConstraint/TangentConstraint_ConvertToTangentConstraint.md), [TangentConstraintProxy.ConvertToTangentConstraint](../TangentConstraintProxy/TangentConstraintProxy_ConvertToTangentConstraint.md), [TangentConstraintProxy.NativeObject](../TangentConstraintProxy/TangentConstraintProxy_NativeObject.md), [TransitionalConstraint.ConvertToTangentConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToTangentConstraint.md), [TransitionalConstraintProxy.ConvertToTangentConstraint](../TransitionalConstraintProxy/TransitionalConstraintProxy_ConvertToTangentConstraint.md), [TranslateTranslateConstraint.ConvertToTangentConstraint](../TranslateTranslateConstraint/TranslateTranslateConstraint_ConvertToTangentConstraint.md), [TranslateTranslateConstraintProxy.ConvertToTangentConstraint](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_ConvertToTangentConstraint.md)

## Derived Classes

[TangentConstraintProxy](../TangentConstraintProxy/TangentConstraintProxy.md)

## Version

Introduced in version 4
