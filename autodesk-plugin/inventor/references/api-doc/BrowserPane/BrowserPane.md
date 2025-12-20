# BrowserPane Object

## Description

The BrowserPane object represents an independent window or panel inside the browser that is currently associated with the active document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../BrowserPane/BrowserPane_Activate.md) | Method that causes the pane to become the active browser pane. |
| [AddBrowserFolder](../BrowserPane/BrowserPane_AddBrowserFolder.md) | Creates a new browser folder at the location specified by the input nodes. |
| [ClearPreSelect](../BrowserPane/BrowserPane_ClearPreSelect.md) | Clears any pre-selection(s) for this pane. |
| [Delete](../BrowserPane/BrowserPane_Delete.md) | Method that deletes the browser pane. If this pane is currently active, the default Inventor pane will become active. This method will fail for built-in browser panes. |
| [GetBrowserNodeFromObject](../BrowserPane/BrowserPane_GetBrowserNodeFromObject.md) | Returns the browser node that corresponds to the input object. The method returns an error if no corresponding node is found within this pane. If multiple matches are found, the method returns the first match. |
| [GetDockingState](../BrowserPane/BrowserPane_GetDockingState.md) | Method that gets the docking state of the browser pane. |
| [Refresh](../BrowserPane/BrowserPane_Refresh.md) | Rebuilds assembly browser by incorporating information from sub-doc(s) default browser pane into the top level document's 'Model' pane. Should be used on a top level assembly's 'Model' pane after a sub-doc's default pane is changed via BrowserPane::Default. |
| [Reorder](../BrowserPane/BrowserPane_Reorder.md) | Moves a node or group of nodes to a new target position within the browser pane. |
| [SetDockingState](../BrowserPane/BrowserPane_SetDockingState.md) | Method that sets the docking state of the browser pane. |
| [Update](../BrowserPane/BrowserPane_Update.md) | Refreshes the browser view. Should be used after changing browser node status (e.g. DisplayState). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../BrowserPane/BrowserPane_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BuiltIn](../BrowserPane/BrowserPane_BuiltIn.md) | Property that specifies if the pane is a standard Inventor pane or not. Built-in panes have restrictions in the edits that can be performed. |
| [Control](../BrowserPane/BrowserPane_Control.md) | Property that returns the ActiveX control that may be associated with the pane. This property will return Nothing in the case this is a Tree Browser Pane. |
| [Default](../BrowserPane/BrowserPane_Default.md) | Specifies if this pane is set as the default when the document is opened. |
| [InternalName](../BrowserPane/BrowserPane_InternalName.md) | Gets either control identifier or the internal identifier depending on whether this browser pane is a ActiveX control identifier or an Inventor tree browser. |
| [Name](../BrowserPane/BrowserPane_Name.md) | Property that gets and sets the name of the pane. When setting the name, an error will occur if the name is not unique with respect to the other panes of the document. The name of built-in panes cannot be set. |
| [Parent](../BrowserPane/BrowserPane_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [SearchBox](../BrowserPane/BrowserPane_SearchBox.md) | Read-only property that gets SearchBox object. |
| [TopNode](../BrowserPane/BrowserPane_TopNode.md) | Gets the top browser node. |
| [TreeBrowser](../BrowserPane/BrowserPane_TreeBrowser.md) | Gets the property that specifies if the pane hosts TreeBrowser nodes constructed by Inventor. |
| [Type](../BrowserPane/BrowserPane_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../BrowserPane/BrowserPane_Visible.md) | Gets and sets the boolean flag which can turn the availability of browser pane in the UI, off or on. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivate](../BrowserPane/BrowserPane_OnActivate.md) | The OnActivate event notifies a client when the BrowserPane has become the active pane. |
| [OnDeactivate](../BrowserPane/BrowserPane_OnDeactivate.md) | The OnDeactivate event notifies a client when a BrowserPane is deactivated. |
| [OnHelp](../BrowserPane/BrowserPane_OnHelp.md) | The OnHelp event notifies a client when the end-user clicks the help button on the browser pane. |

## Accessed From

[BrowserPanes.ActivePane](../BrowserPanes/BrowserPanes_ActivePane.md), [BrowserPanes.Add](../BrowserPanes/BrowserPanes_Add.md), [BrowserPanes.AddByManifest](../BrowserPanes/BrowserPanes_AddByManifest.md), [BrowserPanes.AddTreeBrowserPane](../BrowserPanes/BrowserPanes_AddTreeBrowserPane.md), [BrowserPanes.Item](../BrowserPanes/BrowserPanes_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add assembly occurrences to a new folder](../../sample-programs/BrowserPaneObject_AddBrowserFolder_Sample.md) | Demonstrates assembly occurrences to a new folder |
| [Demote occurence](../../sample-programs/BrowserPaneObject_Reorder_Demote_Sample.md) | This sample demonstrates how to demote a top level occurrence in an assembly into a new sub-assembly occurrence. |
| [Promote occurence](../../sample-programs/BrowserPaneObject_Reorder_Promote_Sample.md) | This sample demonstrates how to promote an occurrence. |
| [Dock browser pane to a custom ViewFrame](../../sample-programs/DockBrowserPaneSample_Sample.md) | This sample demonstrates how to dock the browser pane to a custom ViewFrame. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |