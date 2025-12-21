# OffsetDimConstraintProxy Object

Derived from: [OffsetDimConstraint](../OffsetDimConstraint/OffsetDimConstraint.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Delete.md) | Method that deletes the constraint. |
| [GetReferenceKey](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnchorPoints](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_AnchorPoints.md) | Gets the anchor points of dimension. |
| [Application](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ContainingOccurrence](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [DimensionCenterPoint](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_DimensionCenterPoint.md) | Gets the center of the dimension line. |
| [Driven](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Driven.md) | Gets and sets whether this dimension constraint is driving the geometry or the geometry is defining the value associated with the constraint. |
| [Entity](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Entity.md) | Property that returns the circle or arc being constrained. |
| [Line](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Line.md) | Property that returns the proxy SketchLine being constrained. |
| [LinearDiameter](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_LinearDiameter.md) | Property that returns whether the dimension is a linear diameter style of dimension. |
| [NativeObject](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [Parameter](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Parameter.md) | Property that returns the parameter associated with this dimension constraint. If the Driven property of the constraint is True, this will return a ReferenceParameter object. Otherwise it will return a ModelParameter object. |
| [Parent](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Parent.md) | Property that returns the parent sketch of the object. |
| [TextPoint](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_TextPoint.md) | Gets and sets the position of the dimension text. |
| [Type](../OffsetDimConstraintProxy/OffsetDimConstraintProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 6
