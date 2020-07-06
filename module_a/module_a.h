
#ifndef MODULE_A_H
#define MODULE_A_H

#include <stdint.h>

/**
 * @brief Module A
 * @defgroup module_a Module A
 * @{
 */
/**
 * @brief Get average of three bytes
 *
 * @param a byte one
 * @param b byte two
 * @param c byte three
 * @return int8_t The average of all bytes
 * @satisfy{@req{002}}
 * @satisfy{@req{003}}
 */
int8_t average_three_bytes(int8_t a, int8_t b, int8_t c);

/**
 * @}
 */
#endif /* MODULE_A_H */