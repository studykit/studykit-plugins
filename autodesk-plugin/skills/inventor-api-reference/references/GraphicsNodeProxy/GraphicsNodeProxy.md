# GraphicsNodeProxy Object

Derived from: [GraphicsNode](../GraphicsNode/GraphicsNode.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddComponentGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddComponentGraphics.md) | Method that creates a new ComponentGraphics object based on the input ComponentDefinition. |
| [AddCurveGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddCurveGraphics.md) | Method that creates a new CurveGraphics graphic primitive. |
| [AddLineGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddLineGraphics.md) | Method that creates a new LineGraphics graphic primitive. |
| [AddLineStripGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddLineStripGraphics.md) | Method that creates a new LineStripGraphics graphic primitive. |
| [AddPointGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddPointGraphics.md) | Method that creates a new PointGraphics graphic primitive. |
| [AddScalableTextGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddScalableTextGraphics.md) | Method that creates a new (scalable) TextGraphics graphic primitive. |
| [AddSurfaceGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddSurfaceGraphics.md) | Method that creates a new SurfaceGraphics object based on the input surface(s). |
| [AddTextGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTextGraphics.md) | Method that creates a new TextGraphics graphic primitive. |
| [AddTriangleFanGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTriangleFanGraphics.md) | Method that creates a new TriangleFanGraphics graphic primitive. |
| [AddTriangleGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTriangleGraphics.md) | Method that creates a new TriangleGraphics graphic primitive. |
| [AddTriangleStripGraphics](../GraphicsNodeProxy/GraphicsNodeProxy_AddTriangleStripGraphics.md) | Method that creates a new TriangleStripGraphics graphic primitive. |
| [ClearSlice](../GraphicsNodeProxy/GraphicsNodeProxy_ClearSlice.md) | Method that clears all the slicing applied to the graphics node. |
| [Copy](../GraphicsNodeProxy/GraphicsNodeProxy_Copy.md) | Method that creates a copy of this . The copy has the same property values as the original, a duplicate of all of the graphics primitives, and the CustomRenderStyle has the same values. A new ID is generated for the copy. |
| [Delete](../GraphicsNodeProxy/GraphicsNodeProxy_Delete.md) | Method that deletes the GraphicsNode. This also deletes all associated graphic primitives. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowSliceCapping](../GraphicsNodeProxy/GraphicsNodeProxy_AllowSliceCapping.md) | Specifies that whether this graphics node will display a cap or not when sliced. |
| [AllowSlicing](../GraphicsNodeProxy/GraphicsNodeProxy_AllowSlicing.md) | Specifies that the node participates in slicing of client graphics. |
| [Appearance](../GraphicsNodeProxy/GraphicsNodeProxy_Appearance.md) | Gets and sets the appearance asset associated with the graphics node. |
| [Application](../GraphicsNodeProxy/GraphicsNodeProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ContainingOccurrence](../GraphicsNodeProxy/GraphicsNodeProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Count](../GraphicsNodeProxy/GraphicsNodeProxy_Count.md) | Property that returns the number of graphic primitive objects associated with this GraphicsNode object. |
| [DisplayName](../GraphicsNodeProxy/GraphicsNodeProxy_DisplayName.md) | Read-write Property that gets and sets display name of this graphics node. |
| [ExcludedFromViewAll](../GraphicsNodeProxy/GraphicsNodeProxy_ExcludedFromViewAll.md) | Specifies that the node is not considered when doing a view all. |
| [Id](../GraphicsNodeProxy/GraphicsNodeProxy_Id.md) | Property that returns the Id of the GraphicsNode. |
| [IsTransparentInPlaceEdit](../GraphicsNodeProxy/GraphicsNodeProxy_IsTransparentInPlaceEdit.md) | Read-write Property that gets and sets transparency behavior of this graphics node in inactive mode. |
| [Item](../GraphicsNodeProxy/GraphicsNodeProxy_Item.md) | Returns the specified graphic entity from the collection. |
| [ItemById](../GraphicsNodeProxy/GraphicsNodeProxy_ItemById.md) | Returns the specified GraphicsPrimitive from the collection using its Id as index. |
| [NativeObject](../GraphicsNodeProxy/GraphicsNodeProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OverrideOpacity](../GraphicsNodeProxy/GraphicsNodeProxy_OverrideOpacity.md) | Override Opacity that controls the transparencty of the node. |
| [Parent](../GraphicsNodeProxy/GraphicsNodeProxy_Parent.md) | Property that returns the object this graphics node belongs to. |
| [RangeBox](../GraphicsNodeProxy/GraphicsNodeProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Selectable](../GraphicsNodeProxy/GraphicsNodeProxy_Selectable.md) | Property that specifies whether the GraphicsNode object can be selected when the Select command is running in Inventor. |
| [Transformation](../GraphicsNodeProxy/GraphicsNodeProxy_Transformation.md) | Property that gets and sets the transformation of the GraphicsNode. |
| [Type](../GraphicsNodeProxy/GraphicsNodeProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../GraphicsNodeProxy/GraphicsNodeProxy_Visible.md) | Read-write property that gets and sets whether the GraphicsNode is visible or not. |
| [VisibleInActiveEditObject](../GraphicsNodeProxy/GraphicsNodeProxy_VisibleInActiveEditObject.md) | Read-write property that gets and sets whether this graphics node is visible when the containing object is not the active edit object. A value of True indicates that this node is visible only when the containing object is activated. The value of this property is ignored if the Visible property on GraphicsNode is False. |
| [VisibleInViews](../GraphicsNodeProxy/GraphicsNodeProxy_VisibleInViews.md) | Property that returns a object containing the Views that this graphics node is visible in. If there are no views in the list, the node is visible in all views. Views may be added or removed from the list. This property is ignored if the Visible property on GraphicsNode is False. |

## Version

Introduced in version 2008
