# ApplicationEvents Object

## Description

Inventor::ApplicationEventsSink

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ApplicationEvents/ApplicationEvents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Parent](../ApplicationEvents/ApplicationEvents_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../ApplicationEvents/ApplicationEvents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [OnActivateDocument](../ApplicationEvents/ApplicationEvents_OnActivateDocument.md) | Event that is fired whenever a document is activated. |
| [OnActivateView](../ApplicationEvents/ApplicationEvents_OnActivateView.md) | Event that fires just after a view is activated. |
| [OnActiveProjectChanged](../ApplicationEvents/ApplicationEvents_OnActiveProjectChanged.md) | Fires just before and soon after the active project is changed, supplying the context in which this action is being taken. |
| [OnApplicationOptionChange](../ApplicationEvents/ApplicationEvents_OnApplicationOptionChange.md) | Fires just before and soon after application options are modified. |
| [OnCloseDocument](../ApplicationEvents/ApplicationEvents_OnCloseDocument.md) | Event that is fired whenever a document is closed. |
| [OnCloseView](../ApplicationEvents/ApplicationEvents_OnCloseView.md) | The OnCloseView event notifies a client when a view is closed. An API view is equivalent to an Inventor graphics window. |
| [OnDeactivateDocument](../ApplicationEvents/ApplicationEvents_OnDeactivateDocument.md) | The OnDeactivateDocument event notifies a client when a document is deactivated. |
| [OnDeactivateView](../ApplicationEvents/ApplicationEvents_OnDeactivateView.md) | Fires just after a view is deactivated. |
| [OnDisplayModeChange](../ApplicationEvents/ApplicationEvents_OnDisplayModeChange.md) | The OnDisplayModeChange event notifies a client when the display mode of a view has changed. |
| [OnDocumentChange](../ApplicationEvents/ApplicationEvents_OnDocumentChange.md) | Fires just before the document is changed, supplying the reasons for change and the context in which this action is being taken. |
| [OnInitializeDocument](../ApplicationEvents/ApplicationEvents_OnInitializeDocument.md) | Event that is fired whenever a document is initialized. At the time this event fires, the document is not open yet. Calling methods or properties on the document will force it to open. |
| [OnMigrateDocument](../ApplicationEvents/ApplicationEvents_OnMigrateDocument.md) | Event that is fired whenever a document is being explicitly migrated. |
| [OnMoveApplicationWindow](../ApplicationEvents/ApplicationEvents_OnMoveApplicationWindow.md) | Fires after application main window is moved. |
| [OnMoveView](../ApplicationEvents/ApplicationEvents_OnMoveView.md) | Fires after view window is moved. |
| [OnNewDocument](../ApplicationEvents/ApplicationEvents_OnNewDocument.md) | Event that is fired whenever a new document is created. |
| [OnNewEditObject](../ApplicationEvents/ApplicationEvents_OnNewEditObject.md) | The OnNewEditObject event notifies a client when the edit object is changing. |
| [OnNewView](../ApplicationEvents/ApplicationEvents_OnNewView.md) | The OnNewView event notifies a client when a new View object is created. An API "View" object is equivalent to an Inventor graphics window. |
| [OnOpenDocument](../ApplicationEvents/ApplicationEvents_OnOpenDocument.md) | The OnOpenDocument event notifies a client when a document is opened. |
| [OnQuit](../ApplicationEvents/ApplicationEvents_OnQuit.md) | The OnQuit event notifies a client when Inventor is being shut down. |
| [OnReady](../ApplicationEvents/ApplicationEvents_OnReady.md) | The OnReady event notifies a client when Inventor has completely initialized and is ready for interactive use. |
| [OnResizeApplicationWindow](../ApplicationEvents/ApplicationEvents_OnResizeApplicationWindow.md) | Fires after application main window is resized, or layout is recalculated. |
| [OnResizeView](../ApplicationEvents/ApplicationEvents_OnResizeView.md) | Fires after view window is resized, or window state is changed. |
| [OnRestart32BitHost](../ApplicationEvents/ApplicationEvents_OnRestart32BitHost.md) | This event is fired when the 32BitHost process is restarted. This process is used to host 32-bit processes when running 64-bit Inventor. The primary use of this is to host VBA, which is currently only a 32-bit process. |
| [OnSaveDocument](../ApplicationEvents/ApplicationEvents_OnSaveDocument.md) | The OnSaveDocument notifies a client whenever a document is saved. |
| [OnTerminateDocument](../ApplicationEvents/ApplicationEvents_OnTerminateDocument.md) | The OnTerminateDocument event notifies a client when a document is being terminated. Termination of a document is a complete close of the document. A document terminate corresponds with a document initialize. |
| [OnTranslateDocument](../ApplicationEvents/ApplicationEvents_OnTranslateDocument.md) | The OnTranslateDocument event notifies a client whenever a file is translated into Inventor or an Inventor document is translated out to a non-Inventor file. |
| [OnUndoOpenDocument](../ApplicationEvents/ApplicationEvents_OnUndoOpenDocument.md) | Fires when an open document transaction is undone. |

## Accessed From

[Application.ApplicationEvents](../Application/Application_ApplicationEvents.md), [InventorServer.ApplicationEvents](InventorServer_ApplicationEvents.md), [InventorServerObject.ApplicationEvents](InventorServerObject_ApplicationEvents.md)

## Version

Introduced in version 4
