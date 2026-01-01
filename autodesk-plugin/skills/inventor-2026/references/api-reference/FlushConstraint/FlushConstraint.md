# FlushConstraint Object

Derived from: [AssemblyConstraint](../AssemblyConstraint/AssemblyConstraint.md) Object

## Description

Object that represents a flush assembly constraint.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../FlushConstraint/FlushConstraint_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../FlushConstraint/FlushConstraint_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../FlushConstraint/FlushConstraint_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../FlushConstraint/FlushConstraint_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../FlushConstraint/FlushConstraint_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../FlushConstraint/FlushConstraint_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../FlushConstraint/FlushConstraint_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../FlushConstraint/FlushConstraint_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../FlushConstraint/FlushConstraint_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../FlushConstraint/FlushConstraint_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../FlushConstraint/FlushConstraint_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../FlushConstraint/FlushConstraint_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../FlushConstraint/FlushConstraint_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../FlushConstraint/FlushConstraint_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../FlushConstraint/FlushConstraint_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../FlushConstraint/FlushConstraint_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Application](../FlushConstraint/FlushConstraint_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../FlushConstraint/FlushConstraint_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConstraintLimits](../FlushConstraint/FlushConstraint_ConstraintLimits.md) | Property that returns the ConstraintLimits object that provides access to various limits related settings for the constraint. |
| [DriveSettings](../FlushConstraint/FlushConstraint_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../FlushConstraint/FlushConstraint_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwo](../FlushConstraint/FlushConstraint_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [GeometryOne](../FlushConstraint/FlushConstraint_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../FlushConstraint/FlushConstraint_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../FlushConstraint/FlushConstraint_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../FlushConstraint/FlushConstraint_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [IsDefaultName](../FlushConstraint/FlushConstraint_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../FlushConstraint/FlushConstraint_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../FlushConstraint/FlushConstraint_Name.md) | Gets/Sets the displayable name of this constraint. |
| [OccurrenceOne](../FlushConstraint/FlushConstraint_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../FlushConstraint/FlushConstraint_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Offset](../FlushConstraint/FlushConstraint_Offset.md) | Property that returns the Parameter object that controls the offset distance of the constraint. |
| [Parent](../FlushConstraint/FlushConstraint_Parent.md) | Property that returns the parent of the object. |
| [ResultOfiMate](../FlushConstraint/FlushConstraint_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../FlushConstraint/FlushConstraint_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [Suppressed](../FlushConstraint/FlushConstraint_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [Type](../FlushConstraint/FlushConstraint_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../FlushConstraint/FlushConstraint_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Accessed From

[AngleConstraint.ConvertToFlushConstraint](../AngleConstraint/AngleConstraint_ConvertToFlushConstraint.md), [AngleConstraintProxy.ConvertToFlushConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToFlushConstraint.md), [AssemblyConstraint.ConvertToFlushConstraint](../AssemblyConstraint/AssemblyConstraint_ConvertToFlushConstraint.md), [AssemblyConstraints.AddFlushConstraint](../AssemblyConstraints/AssemblyConstraints_AddFlushConstraint.md), [AssemblySymmetryConstraint.ConvertToFlushConstraint](../AssemblySymmetryConstraint/AssemblySymmetryConstraint_ConvertToFlushConstraint.md), [AssemblySymmetryConstraintProxy.ConvertToFlushConstraint](../AssemblySymmetryConstraintProxy/AssemblySymmetryConstraintProxy_ConvertToFlushConstraint.md), [CustomConstraint.ConvertToFlushConstraint](CustomConstraint_ConvertToFlushConstraint.md), [CustomConstraintProxy.ConvertToFlushConstraint](CustomConstraintProxy_ConvertToFlushConstraint.md), [FlushConstraint.ConvertToFlushConstraint](../FlushConstraint/FlushConstraint_ConvertToFlushConstraint.md), [FlushConstraintProxy.ConvertToFlushConstraint](../FlushConstraintProxy/FlushConstraintProxy_ConvertToFlushConstraint.md), [FlushConstraintProxy.NativeObject](../FlushConstraintProxy/FlushConstraintProxy_NativeObject.md), [InsertConstraint.ConvertToFlushConstraint](../InsertConstraint/InsertConstraint_ConvertToFlushConstraint.md), [InsertConstraintProxy.ConvertToFlushConstraint](../InsertConstraintProxy/InsertConstraintProxy_ConvertToFlushConstraint.md), [LayoutConstraint.XYFlushConstraint](../LayoutConstraint/LayoutConstraint_XYFlushConstraint.md), [LayoutConstraint.XZFlushConstraint](../LayoutConstraint/LayoutConstraint_XZFlushConstraint.md), [LayoutConstraint.YZFlushConstraint](../LayoutConstraint/LayoutConstraint_YZFlushConstraint.md), [LayoutConstraintProxy.XYFlushConstraint](../LayoutConstraintProxy/LayoutConstraintProxy_XYFlushConstraint.md), [LayoutConstraintProxy.XZFlushConstraint](../LayoutConstraintProxy/LayoutConstraintProxy_XZFlushConstraint.md), [LayoutConstraintProxy.YZFlushConstraint](../LayoutConstraintProxy/LayoutConstraintProxy_YZFlushConstraint.md), [MateConstraint.ConvertToFlushConstraint](../MateConstraint/MateConstraint_ConvertToFlushConstraint.md), [MateConstraintProxy.ConvertToFlushConstraint](../MateConstraintProxy/MateConstraintProxy_ConvertToFlushConstraint.md), [RotateRotateConstraint.ConvertToFlushConstraint](../RotateRotateConstraint/RotateRotateConstraint_ConvertToFlushConstraint.md), [RotateRotateConstraintProxy.ConvertToFlushConstraint](../RotateRotateConstraintProxy/RotateRotateConstraintProxy_ConvertToFlushConstraint.md), [RotateTranslateConstraint.ConvertToFlushConstraint](../RotateTranslateConstraint/RotateTranslateConstraint_ConvertToFlushConstraint.md), [RotateTranslateConstraintProxy.ConvertToFlushConstraint](../RotateTranslateConstraintProxy/RotateTranslateConstraintProxy_ConvertToFlushConstraint.md), [TangentConstraint.ConvertToFlushConstraint](../TangentConstraint/TangentConstraint_ConvertToFlushConstraint.md), [TangentConstraintProxy.ConvertToFlushConstraint](../TangentConstraintProxy/TangentConstraintProxy_ConvertToFlushConstraint.md), [TransitionalConstraint.ConvertToFlushConstraint](../TransitionalConstraint/TransitionalConstraint_ConvertToFlushConstraint.md), [TransitionalConstraintProxy.ConvertToFlushConstraint](../TransitionalConstraintProxy/TransitionalConstraintProxy_ConvertToFlushConstraint.md), [TranslateTranslateConstraint.ConvertToFlushConstraint](../TranslateTranslateConstraint/TranslateTranslateConstraint_ConvertToFlushConstraint.md), [TranslateTranslateConstraintProxy.ConvertToFlushConstraint](../TranslateTranslateConstraintProxy/TranslateTranslateConstraintProxy_ConvertToFlushConstraint.md)

## Derived Classes

[FlushConstraintProxy](../FlushConstraintProxy/FlushConstraintProxy.md)

## Version

Introduced in version 4
