# AngleConstraintProxy Object

Derived from: [AngleConstraint](../AngleConstraint/AngleConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToAngleConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToAngleConstraint.md) | Method that converts the constraint to an angle constraint, and returns the AngleConstraint object. This method can also be used to edit the geometries associated with an angle constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToCustomConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToCustomConstraint.md) | Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToFlushConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToFlushConstraint.md) | Method that converts the constraint to a flush constraint, and returns the FlushConstraint object. This method can also be used to edit the geometries associated with a flush constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToInsertConstraint.md) | Method that converts the constraint to an insert constraint, and returns the InsertConstraint object. This method can also be used to edit the geometries associated with an insert constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToInsertConstraint2](../AngleConstraintProxy/AngleConstraintProxy_ConvertToInsertConstraint2.md) | Converts the constraint to an insert constraint, and returns the InsertConstraint object. |
| [ConvertToMateConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToMateConstraint.md) | Method that converts the constraint to a mate constraint, and returns the MateConstraint object. This method can also be used to edit the geometries associated with a mate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToMateConstraint2](../AngleConstraintProxy/AngleConstraintProxy_ConvertToMateConstraint2.md) | Converts the constraint to a mate constraint, and returns the MateConstraint object. |
| [ConvertToRotateRotateConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToRotateRotateConstraint.md) | Method that converts the constraint to a rotate-rotate constraint, and returns the RotateRotateConstraint object. This method can also be used to edit the geometries associated with a rotate-rotate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToRotateTranslateConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToRotateTranslateConstraint.md) | Method that converts the constraint to a rotate-translate constraint, and returns the RotateTranslateConstraint object. This method can also be used to edit the geometries associated with a rotate-translate constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToSymmetryConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToSymmetryConstraint.md) | Converts the constraint to a symmetry constraint, and returns the AssemblySymmetryConstraint object. |
| [ConvertToTangentConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToTangentConstraint.md) | Method that converts the constraint to a tangent constraint, and returns the TangentConstraint object. This method can also be used to edit the geometries associated with a tangent constraint without changing its type, in which case the same object is returned by the method. |
| [ConvertToTransitionalConstraint](../AngleConstraintProxy/AngleConstraintProxy_ConvertToTransitionalConstraint.md) | Method that converts the constraint to a transitional constraint, and returns the TransitionalConstraint object. This method can also be used to edit the geometries associated with a transitional constraint without changing its type, in which case the same object is returned by the method. |
| [Delete](../AngleConstraintProxy/AngleConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../AngleConstraintProxy/AngleConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AffectedOccurrenceOne](../AngleConstraintProxy/AngleConstraintProxy_AffectedOccurrenceOne.md) | Property that returns the first of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceOne property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the first of the two geometries that this constraint is between. |
| [AffectedOccurrenceTwo](../AngleConstraintProxy/AngleConstraintProxy_AffectedOccurrenceTwo.md) | Property that returns the second of the two objects affected by this constraint. This is the same as the owning occurrence obtained from the OccurrenceTwo property in the case where the owning assembly is not adaptive. Else, this is the first non-adaptive occurrence in the path leading from the owning occurrence to the occurrence that contains the second of the two geometries that this constraint is between. |
| [Angle](../AngleConstraintProxy/AngleConstraintProxy_Angle.md) | Property that returns the object that controls the angle of the constraint. |
| [Application](../AngleConstraintProxy/AngleConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../AngleConstraintProxy/AngleConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConstraintLimits](../AngleConstraintProxy/AngleConstraintProxy_ConstraintLimits.md) | Property that returns the ConstraintLimits object that provides access to various limits related settings for the constraint. |
| [ContainingOccurrence](../AngleConstraintProxy/AngleConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DriveSettings](../AngleConstraintProxy/AngleConstraintProxy_DriveSettings.md) | Returns the DriveSettings object for the constraint. |
| [EntityOne](../AngleConstraintProxy/AngleConstraintProxy_EntityOne.md) | Property that indicates the first of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [EntityTwo](../AngleConstraintProxy/AngleConstraintProxy_EntityTwo.md) | Property that indicates the second of the geometric entities (Face, Axis, Edge, etc.) being constrained. |
| [GeometryOne](../AngleConstraintProxy/AngleConstraintProxy_GeometryOne.md) | Property that returns the geometry of the first of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [GeometryTwo](../AngleConstraintProxy/AngleConstraintProxy_GeometryTwo.md) | Property that returns the geometry of the second of the two entities that this constraint is between. The geometry returned is in the space of the assembly and for face or work plane geometries it accounts for the orientation of the face or work plane. |
| [HealthStatus](../AngleConstraintProxy/AngleConstraintProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [iMateResult](../AngleConstraintProxy/AngleConstraintProxy_iMateResult.md) | Property that returns the iMateResult object that resulted in the creation of this constraint. |
| [IsDefaultName](../AngleConstraintProxy/AngleConstraintProxy_IsDefaultName.md) | Indicates if the name of this constraint is the original default name or if the user has changed the name. A value of True indicates the name is the original default name. |
| [LayoutConstraint](../AngleConstraintProxy/AngleConstraintProxy_LayoutConstraint.md) | Property that returns the layout constraint this constraint is a member of. Returns Nothing in the case where this constraint is not a member of a layout constraint. You can also determine if a constraint is a member of a layout constraint by using the ResultOfLayoutConstraint property. |
| [Name](../AngleConstraintProxy/AngleConstraintProxy_Name.md) | Gets/Sets the displayable name of this constraint. |
| [NativeObject](../AngleConstraintProxy/AngleConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OccurrenceOne](../AngleConstraintProxy/AngleConstraintProxy_OccurrenceOne.md) | Property that returns the first of the two objects this constraint is between. |
| [OccurrenceTwo](../AngleConstraintProxy/AngleConstraintProxy_OccurrenceTwo.md) | Property that returns the second of the two objects this constraint is between. |
| [Parent](../AngleConstraintProxy/AngleConstraintProxy_Parent.md) | Property that returns the parent of the object. |
| [ReferenceVectorEntity](../AngleConstraintProxy/AngleConstraintProxy_ReferenceVectorEntity.md) | Property that returns the third (reference vector) entity the constraint it tied to. |
| [ResultOfiMate](../AngleConstraintProxy/AngleConstraintProxy_ResultOfiMate.md) | Property that indicates if this iMateResult represents a composite iMate. |
| [ResultOfLayoutConstraint](../AngleConstraintProxy/AngleConstraintProxy_ResultOfLayoutConstraint.md) | Property that indicates if this constraint is a member of a layout constraint. If True then it is a member of a layout constraint. The layout constraint can be obtained by using the LayoutConstraint property. |
| [SolutionType](../AngleConstraintProxy/AngleConstraintProxy_SolutionType.md) | Property that returns the solution type. |
| [Suppressed](../AngleConstraintProxy/AngleConstraintProxy_Suppressed.md) | Gets/Sets the Boolean flag indicating whether this constraint is suppressed. |
| [Type](../AngleConstraintProxy/AngleConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../AngleConstraintProxy/AngleConstraintProxy_Visible.md) | Gets/Sets the Visible indicating whether this constraint is visible. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |