
(set-language-environment "UTF-8")

;; To debug 
;;(setq debug-on-error t)

; Activation de la molette de la souris
(require 'mwheel)
(mwheel-install) 

;; Utiliser les time-stamps d'emacs
(defun insert-date ()
"Insert date at point."
(interactive)
(insert (format-time-string "%A %e %B %Y, %R")))
(global-set-key [f9] 'insert-date)
(add-hook 'write-file-hooks 'time-stamp)

(setq time-stamp-active t)

;; GNU coding standard Key-Bindings
(global-set-key [f1] 'dired)
(global-set-key [f2] 'dired-omit-mode)
(global-set-key [f3] 'shell)
(global-set-key [f4] 'find-file)
(global-set-key [f5] 'compile)
(global-set-key [f6] 'visit-tags-table)
(global-set-key [f8] 'add-change-log-entry-other-window)
(global-set-key [f12] 'make-frame)

;; My Key-Bindings
(global-set-key [pause] 'kill-buffer)
(global-set-key [f11] 'kill-buffer)

(global-set-key "\C-xw" 'what-line)
(global-set-key [f7] 'save-buffer)
(global-set-key [home] 'beginning-of-buffer)
(global-set-key [end] 'end-of-buffer)
(global-set-key "\C-c\C-c" 'compile)
(global-set-key "\C-f" 'toggle-frame-fullscreen)

(global-set-key (kbd "C-x <up>") 'windmove-up)
(global-set-key (kbd "C-x <down>") 'windmove-down)
(global-set-key (kbd "C-x <right>") 'windmove-right)
(global-set-key (kbd "C-x <left>") 'windmove-left)

;; Always end a file with a newline
(setq require-final-newline t)

;; Stop at the end of the file, not just add lines
(setq next-line-add-newlines nil)

;; line number is displayed in mode line.
(line-number-mode 1) 
(column-number-mode 1) 

;; Turn on font-lock mode for Emacs and similar stuff
(setq-default visible-bell t)
(setq default-major-mode 'text-mode)
(add-hook 'text-mode-hook 'turn-on-auto-fill)

;; Number of column that the text is justified to 
(setq-default fill-column 80)

;; Default font. Now using emacsclient, must use this format instead:
(add-to-list 'default-frame-alist '(font . "Inconsolata-14"))
;;(set-default-font "DejaVu Sans Mono-12")
;;(add-to-list 'default-frame-alist '(font . "DejaVu Sans Mono-12"))

(global-font-lock-mode t)
;;(setq font-lock-support-mode 'fast-lock-mode) ; caching on End Colours
;;(setq font-lock-support-mode 'lazy-lock-mode)

;;; Put the buffer name in the titlebar
(setq frame-title-format "%b")

;; Highlight Parenthesis
(require 'paren)
(show-paren-mode 1)

;; Latex configuration
;; -------------------
(require 'tex-site)

;; To have auctex compile to pdf by default
(setq TeX-PDF-mode t)

;; For multiple files documents --> auctex always ask for a master
;; file when opening a .tex document.
(setq-default TeX-master nil)
;; This makes AucTex parse buffers and create the auto backup directory
(setq TeX-parse-self t) ; Enable parse on load.
(setq TeX-auto-save t) ; Enable parse on save.
;; Convert tabs to spaces (latex only)
(setq TeX-auto-untabify t)

;; This is to manage references (\ref and \label) in a .tex document
(autoload 'reftex-mode    "reftex" "RefTeX Minor Mode" t)
(autoload 'turn-on-reftex "reftex" "RefTeX Minor Mode" t)
(add-hook 'LaTeX-mode-hook 'turn-on-reftex) ; with AUCTeX LaTeX mode
